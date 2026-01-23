HTTPS Deployment Guide:
1. Obtain SSL certificates (e.g., via Let's Encrypt).
2. In Nginx, set 'listen 443 ssl'.
3. Point 'ssl_certificate' and 'ssl_certificate_key' to your files.
4. Ensure the proxy_set_header X-Forwarded-Proto $scheme; is set so Django knows the connection is secure.