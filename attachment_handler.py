import hashlib
import os

def save_and_hash_attachments(msg):
    hashes = []

    for part in msg.walk():
        if part.get_content_disposition() == "attachment":
            filename = part.get_filename()
            if not filename:
                continue

            file_data = part.get_payload(decode=True)

            filepath = f"attachments/{filename}"
            os.makedirs("attachments", exist_ok=True)

            with open(filepath, "wb") as f:
                f.write(file_data)

            sha256 = hashlib.sha256(file_data).hexdigest()
            hashes.append(sha256)

    return hashes