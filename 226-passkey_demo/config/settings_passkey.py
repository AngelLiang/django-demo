# Change your authentication backend
import passkeys

AUTHENTICATION_BACKENDS = ['passkeys.backend.PasskeyModelBackend']
# Server rp id for FIDO2, it the full domain of your project
FIDO_SERVER_ID = "localhost"
FIDO_SERVER_NAME = "TestApp"

# KEY_ATTACHMENT = None | passkeys.Attachment.CROSS_PLATFORM | passkeys.Attachment.PLATFORM
KEY_ATTACHMENT = passkeys.Attachment.CROSS_PLATFORM
