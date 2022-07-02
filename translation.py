class Translation(object):
    START_TEXT = """⭐ Hi {} \n 😉 Soy URL UPLOADER perteneciente a la cadena de bots R-DOWNLOAD \n 👉 Soy el encargado de extraer los vídeos o archivos de una url (youtube, facebook, etc) y subirlos a Telegram \n 👉 Use /help para saber más sobre mi
\help -£> Informacion!"""
    FORMAT_SELECTION = "Seleccione el formato deseado: <a href='{}'>El tamaño del archivo puede ser aproximado</a> \n Si desea establecer una miniatura personalizada, envíe una foto antes o rápidamente después de tocar cualquiera de los botones a continuación.\nPuedes usar /deletethumbnail para eliminar las miniaturas generadas automaticamente."
    SET_CUSTOM_USERNAME_PASSWORD = """Si deseas descargar videos Premium proporcione de esta forma:
URL | filename | username | password"""
    DOWNLOAD_START = "⬇ DESCARGANDO ..."
    UPLOAD_START = "⬆ SUBIENDO ..."
    RCHD_TG_API_LIMIT = "⏰ Descargado en {} seconds.\n 📄 Tamaño del Archivo: {}\nSorry. La API de Telegram solo permite archivos menores a 2GB."
    AFTER_SUCCESSFUL_UPLOAD_MSG = "😍 Gracias por usar URL UPLOADER)"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "⏰ Descargado {} seconds.\n ⬆ Subido en  {} seconds.\n\n ⚡️ URL UPLOADER ⚡️"
    SAVED_CUSTOM_THUMB_NAIL = "Miniatura de video / file thumbnail saved. Esta imagen será usada en el video / file."
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ Miniatura eliminada satisfactoriamente."
    CUSTOM_CAPTION_UL_FILE = "{}"
    NO_VOID_FORMAT_FOUND = "ERROR...\n<b>YouTubeDL</b> said: {}"
    HELP_USER = """Como usarme? Sigue estos pasos!
    
1. Enviame un enlace
2. (Opcional) Si quieres que renombre el archivo o video enviamelo de esta forma 👉 https://enlace.del.video | nuevo_nombre.mp4
3. (Opcional) Enviame una imagen para usarlo de miniatura
4. Selecciona el botón.
   SVideo - Dar el archivo como video con capturas de pantallas.
   DFile  - Dar el archivo (video) como archivo y con capturas de pantallas
   Video  - Dar el archivo como video sin capturas de pantallas
   File   - Dar como archivo sin capturas de pantallas

Si el bot no responde, contacta con @raydel0307"""
    REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = "Responde con /genthumbnail a un álbum de medios para generar capturas de pantallas"
    ERR_ONLY_TWO_MEDIA_IN_ALBUM = "El álbum de medios debe contener solo dos fotos. Vuelva a enviar el álbum de medios y luego intente nuevamente, o envíe solo dos fotos en un album."
    CANCEL_STR = "❌ Proceso cancelado"
    ZIP_UPLOADED_STR = "⬆ Subidos {} 📄 archivos en {} ⏰ segundos"
    SLOW_URL_DECED = "Dios, eso parece ser una URL muy lenta. Dado que estaba jodiendo mi casa, no estoy de humor para descargar este archivo. Mientras tanto, ¿por qué no intentas conseguirme una URL rápida para que pueda subir a Telegram, sin que me desacelere para otros usuarios "
