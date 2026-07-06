import webbrowser


class WebLauncher:

    def __init__(self):
        self.websites = {
            "google": "https://www.google.com",
            "youtube": "https://www.youtube.com",
            "chatgpt": "https://chat.openai.com",
            "github": "https://github.com",
            "linkedin": "https://www.linkedin.com",
            "gmail": "https://mail.google.com",
            "instagram": "https://www.instagram.com",
            "facebook": "https://www.facebook.com",
            "x": "https://x.com",
            "spotify": "https://open.spotify.com"
        }

    def open(self, website):

        website = website.lower()

        if website in self.websites:
            webbrowser.open(self.websites[website])
            return True

        return False