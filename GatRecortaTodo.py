

def acortar_url():
    original_url = input("Ingrese la URL original: ")
    personalization = input("Ingrese la personalización (opcional): ").strip()
    api_url = f'https://is.gd/create.php?format=json&url={requests.utils.quote(original_url)}'

    if personalization:
        api_url += f'&shorturl={requests.utils.quote(personalization)}'

    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Esto lanzará un error para códigos de estado HTTP 4xx/5xx
        data = response.json()

        if 'shorturl' in data:
            print(f'URL acortada: {data["shorturl"]}')
            return data["shorturl"]
        else:
            print('Error al acortar la URL. Detalles:', data)
    except requests.exceptions.RequestException as e:
        print('Error en la solicitud:', e)
    except ValueError as e:
        print('Error al procesar la respuesta:', e)
    return None

def obtener_informacion_url(short_url):
    if short_url:
        api_url = f'https://is.gd/stats.php?url={short_url[-6:]}&format=json'
        try:
            response = requests.get(api_url)
            response.raise_for_status()
            data = response.json()
            if 'url' in data:
                print("Información de la URL:")
                print(f"URL original: {data['url']}")
                print(f"URL acortada: {data['shorturl']}")
                print(f"Clicks: {data['clicks']}")
            else:
                print('Error al obtener la información de la URL. Detalles:', data)
        except requests.exceptions.RequestException as e:
            print('Error en la solicitud:', e)
        except ValueError as e:
            print('Error al procesar la respuesta:', e)
    else:
        print('Link del grupo de Telegram : https://t.me/+sOf-gqn6SClmNDcx')

def menu():
    short_url = None
    banner = r"""
           ／＞-.-フ
　　　　　| 　_　 _l
　 　　　／` ミ＿xノ
　　 　 /　　　 　 |
　　　 /　 ヽ　　 ﾉ
　／￣|　　 |　 |  |
　| (￣ヽ＿_ヽ__) _)
　＼二つ
 By AvastrOficial / Version : 0.0.1
"""
    while True:
        print(banner)
        print("GatRecortaTodo :")
        print("1. Recortar URL")
        print("2. Informacion")
        print("3. Salir")
        print(" ")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            short_url = acortar_url()
        elif opcion == '2':
            obtener_informacion_url(short_url)
        elif opcion == '3':
            print("Saliendo de la herramienta...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")

if __name__ == "__main__":
    menu()
