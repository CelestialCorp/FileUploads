import os

class Config:
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'pdf', 'mp3', 'wav', 'txt', 'docx', 'pptx'}
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB limite massimo per i file
