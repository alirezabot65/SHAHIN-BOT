import requests

class RubikaBotAPI:
    def __init__(self, token):
        self.token = token
        self.base = f"https://botapi.rubika.ir/v3/{token}"

    def _post(self, method, payload=None):
        try:
            r = requests.post(f"{self.base}/{method}", json=payload or {}, timeout=10)
            return r.json()
        except Exception as e:
            return {"ok": False, "error": str(e)}

    def get_me(self):
        return self._post("getMe")

    def send_message(self, chat_id, text):
        return self._post("sendMessage", {"chat_id": chat_id, "text": text})
