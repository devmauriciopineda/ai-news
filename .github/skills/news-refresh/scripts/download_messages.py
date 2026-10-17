"""Download new newsletter emails to app/news as Markdown, per sender."""

import email
import imaplib
import json
import sys
from datetime import date, timedelta, timezone
from email.header import decode_header, make_header
from email.utils import parsedate_to_datetime
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[4]
NEWS_DIR = PROJECT_ROOT / "app" / "news"
INITIAL_DAYS = 7
SENDERS = {
    "AlphaSignal": "news@alphasignal.ai",
    "AheadOfAI": "sebastianraschka@substack.com",
    "ChinAI": "chinai@substack.com",
    "DeepLearningWeekly": "deeplearningweekly@substack.com",
    "ImportAI": "importai@substack.com",
    "Interconnects": "robotic@substack.com",
    "LastWeekInAI": "lastweekinai+news@substack.com",
    "RundownAI": "news@daily.therundown.ai",
    "Substack": "no-reply@substack.com",
    "Superhuman": "superhuman@mail.joinsuperhuman.ai",
    "TheMedian": "dcthemedian@substack.com",
    "TheNeuron": "theneuron@newsletter.theneurondaily.com",
    "TLDR": "dan@tldrnewsletter.com",
    "UnderstandingAI": "understandingai@substack.com",
    "UnderstandingRobots": "understandingrobots@substack.com",
}
# Suffixes written before per-sender labels existed.
LEGACY_SUFFIXES = {"AlphaSignal": "AlphaSignalNews"}
sys.path.insert(0, str(PROJECT_ROOT))

from app.core.config import settings  # noqa: E402


def message_timestamp(sent_at):
    try:
        parsed = parsedate_to_datetime(sent_at)
        if parsed.tzinfo is not None:
            parsed = parsed.astimezone(timezone.utc)
        return parsed.strftime("%Y%m%d_%H%M%S")
    except (TypeError, ValueError, OverflowError):
        return f"{date.today():%Y%m%d}_000000"


def watermark(label):
    if not NEWS_DIR.exists():
        return None
    suffixes = {label, LEGACY_SUFFIXES.get(label, label)}
    stamps = [
        path.stem[:15]
        for path in NEWS_DIR.glob("????????_??????_*.md")
        if path.stem[16:] in suffixes
    ]
    return max(stamps, default=None)


def search_start(latest):
    if latest is None:
        return date.today() - timedelta(days=INITIAL_DAYS)
    return date(int(latest[:4]), int(latest[4:6]), int(latest[6:8]))


def decode_message(raw_message):
    message = email.message_from_bytes(raw_message)
    subject = str(make_header(decode_header(message.get("Subject", ""))))
    sender = message.get("From", "")
    sent_at = message.get("Date", "")
    body = ""
    parts = message.walk() if message.is_multipart() else (message,)

    for part in parts:
        if part.get_content_type() != "text/plain":
            continue
        payload = part.get_payload(decode=True)
        if payload is not None:
            body = payload.decode(
                part.get_content_charset() or "utf-8",
                errors="replace",
            )
        break

    return subject, sender, sent_at, body


def render_message(subject, sender, sent_at, body):
    return "\n".join(
        [
            f"# {subject}",
            "",
            f"- De: {sender}",
            f"- Fecha: {sent_at}",
            "",
            body.rstrip(),
        ]
    )


def download_mailbox(mail, mailbox, address, label, since, latest):
    if mail.select(mailbox, readonly=True)[0] != "OK":
        raise RuntimeError(f"No se pudo seleccionar el buzón {mailbox!r}.")
    status, result = mail.uid("search", None, "FROM", address, "SINCE", since)
    if status != "OK":
        raise RuntimeError(f"Falló la búsqueda IMAP en {mailbox!r}.")

    saved = []
    for uid in result[0].split():
        status, response = mail.uid("fetch", uid, "(BODY.PEEK[])")
        if status != "OK":
            raise RuntimeError(f"No se pudo recuperar el UID {uid!r}.")
        raw_message = next(
            (part[1] for part in response if isinstance(part, tuple)),
            None,
        )
        if raw_message is None:
            raise RuntimeError(f"La respuesta no incluyó el UID {uid!r}.")

        subject, sender, sent_at, body = decode_message(raw_message)
        timestamp = message_timestamp(sent_at)
        if latest and timestamp <= latest:
            continue

        NEWS_DIR.mkdir(parents=True, exist_ok=True)
        path = NEWS_DIR / f"{timestamp}_{label}.md"
        if path.exists():
            continue
        path.write_text(
            render_message(subject, sender, sent_at, body),
            encoding="utf-8",
        )
        saved.append(path.relative_to(PROJECT_ROOT).as_posix())
    return saved


def main():
    downloaded = []

    with imaplib.IMAP4_SSL("imap.gmail.com") as mail:
        mail.login(
            settings.gmail_email,
            settings.gmail_application_password.get_secret_value(),
        )
        for label, address in SENDERS.items():
            latest = watermark(label)
            since = search_start(latest).strftime("%d-%b-%Y")
            for mailbox in ("INBOX", f"InfoIA/{label}"):
                downloaded.extend(
                    download_mailbox(
                        mail, mailbox, address, label, since, latest
                    )
                )

    print(
        json.dumps(
            {
                "downloaded": downloaded,
                "summary_sources": downloaded,
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
