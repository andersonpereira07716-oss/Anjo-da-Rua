import os
import glob

print("Procurando APKs na pasta do projeto...")
apks = glob.glob("**/app-debug.apk", recursive=True) + glob.glob("**/app-release.apk", recursive=True) + glob.glob("**/*.apk", recursive=True)

if not apks:
    print("\nAviso: Nenhum APK encontrado localmente na pasta.")
    print("Lembra-te que o APK é compilado na nuvem pelo GitHub Actions.")
    print("Podes descarregá-lo do GitHub e guardá-lo na pasta de Downloads (/sdcard/Download/).")
else:
    for apk in apks:
        print(f"APK localizado: {apk}")
        # Copiar para o armazenamento interno do Android (Pasta Download)
        destino = f"/sdcard/Download/{os.path.basename(apk)}"
        os.system(f"cp '{apk}' '{destino}'")
        print(f"Copiado com sucesso para o telemóvel: {destino}")
        print("Podes agora abrir a aplicação do Google Drive no telemóvel e fazer o upload direto do ficheiro na pasta Downloads!")
