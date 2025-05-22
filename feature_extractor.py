from urllib.parse import urlparse

def extract_features(url):
    parsed = urlparse(url)
    features = [
        len(url),                          # URL length
        url.count('.'),                    # Dot count
        int('https' in url.lower()),       # HTTPS
        int('@' in url),                   # @ symbol
        len(parsed.netloc),                # Domain length
        int('-' in parsed.netloc),         # Hyphen
        int('//' in url),                  # Double slash
        int(parsed.netloc.replace('.', '').isdigit())  # Numeric domain
    ]
    return features
