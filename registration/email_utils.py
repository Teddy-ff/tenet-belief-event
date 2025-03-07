import qrcode
from io import BytesIO
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def send_squid_game_email(user_email, user_name, player_number):
    """Send Squid Game themed email with player number and QR code."""

    # Generate QR Code (Containing player number for event check-in)
    qr_data = f"Player Number: {player_number:03}\nName: {user_name}"
    qr = qrcode.make(qr_data)
    qr_io = BytesIO()
    qr.save(qr_io, format='PNG')
    qr_io.seek(0)
    qr_image_data = qr_io.getvalue()

    # Render Email Template
    email_html = render_to_string('squid_game_email.html', {
        'user_name': user_name,
        'player_number': f"{player_number:03}",  # Format as 001, 002, etc.
        'qr_code_url': 'cid:qr_code'
    })
    email_plain = strip_tags(email_html)

    # Send Email
    email = EmailMessage(
    subject=f"🔴 Welcome, Player {player_number:03}! Your Squid Game Challenge Awaits",
    body=email_html,  # Use the rendered HTML content
    from_email='your-email@gmail.com',
    to=[user_email]
)
    email.content_subtype = "html"  # ✅ Ensure the email is sent as HTML
    email.attach("qr_code.png", qr_image_data, "image/png")  # Attach QR Code
    email.send()


    print(f"Email sent to Player {player_number:03}: {user_email}")
