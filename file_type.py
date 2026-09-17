import os

def emoji_arquivo(nome_arquivo: str) -> str:
    ext = os.path.splitext(nome_arquivo)[1].lower()

    emojis = {
        # Documentos
        '.pdf': '📕', '.doc': '📄', '.docx': '📄', '.txt': '📝', '.md': '📝',
        '.xls': '📊', '.xlsx': '📊', '.csv': '📊',
        '.ppt': '📽️', '.pptx': '📽️',
        # Imagens
        '.jpg': '🖼️', '.jpeg': '🖼️', '.png': '🖼️', '.gif': '🖼️',
        '.svg': '🖼️', '.webp': '🖼️', '.bmp': '🖼️',
        # Áudio
        '.mp3': '🎵', '.wav': '🎵', '.flac': '🎵', '.ogg': '🎵',
        # Vídeo
        '.mp4': '🎬', '.avi': '🎬', '.mov': '🎬', '.mkv': '🎬',
        # Compactados
        '.zip': '🗜️', '.rar': '🗜️', '.7z': '🗜️', '.tar': '🗜️', '.gz': '🗜️',
        # Código
        '.py': '🐍', '.js': '📜', '.html': '🌐', '.css': '🎨',
        '.json': '🧾', '.xml': '🧾', '.java': '☕', '.c': '⚙️', '.cpp': '⚙️',
        '.sh': '💻', '.sql': '🗄️',
        # Executáveis
        '.exe': '⚙️', '.apk': '📱', '.dmg': '💿', '.iso': '💿',
        # Fontes
        '.ttf': '🔤', '.otf': '🔤',
    }

    return emojis.get(ext, '📁')