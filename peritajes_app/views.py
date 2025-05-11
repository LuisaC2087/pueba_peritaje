from django.shortcuts import render
from django.http import HttpResponse
from weasyprint import HTML, CSS
from django.conf import settings
from django.templatetags.static import static
from datetime import datetime
from django.contrib.staticfiles import finders
from django.template.loader import get_template
import os
from PIL import Image, ImageResampling
from io import BytesIO


def home(request):
    return render(request, 'index.html')


def generar_pdf(request):
    if request.method == 'POST':

        # Obtener listas de marcas y descripciones desde el formulario
        marcas = request.POST.getlist("marca[]") 
        descripciones = request.POST.getlist("descripcion[]")  

        # Combinar marcas y descripciones en un diccionario
        accesorios = [{"marca": marca, "descripcion": descripcion} for marca, descripcion in zip(marcas, descripciones)]

        fecha = request.POST.get('fecha')

        if fecha:
            fecha = datetime.strptime(fecha, "%Y-%m-%d").strftime("%d-%m-%Y")

        datos = {
            # Información general
            'fecha': fecha,
            'placa_carro': request.POST.get('placa_carro'),
            
            # Datos del vehículo
            'cliente': request.POST.get('cliente'),
            'marca': request.POST.get('marca'),
            'modelo': request.POST.get('modelo'),
            'kilometraje': request.POST.get('kilometraje'),
            'linea': request.POST.get('linea'),
            'tipo_caja': request.POST.get('tipo_caja'),
            'color': request.POST.get('color'),
            'cilindraje': request.POST.get('cilindraje'),
            'combustible': request.POST.get('combustible'),
            'servicio': request.POST.get('servicio'),
            'categoria': request.POST.get('categoria'),
            'carroceria': request.POST.get('carroceria'),

            #Latoneria y pintura
            "capot_seleccionado": request.POST.getlist("capot[]"),
            "torpedo_seleccionado": request.POST.getlist("torpedo[]"),
            "bomper_del_seleccionado": request.POST.getlist("bomper_del[]"),
            "guarda_fango": request.POST.getlist("guarda_fango[]"),
            "estribo_izq_seleccionado": request.POST.getlist("estribo_izq[]"),
            "puerta_del_izq_seleccionado": request.POST.getlist("puerta_del_izq[]"),
            "puerta_trasera_izq_seleccionado": request.POST.getlist("puerta_trasera_izq[]"),
            "guardabarro_tras_izq": request.POST.getlist("guardabarro_tras_izq[]"),
            "bomper_tra_seleccionado": request.POST.getlist("bomper_tra[]"),
            "alma_bomper_tra_seleccionado": request.POST.getlist("alma_bomper_tra[]"),
            "tapa_baul_seleccionado": request.POST.getlist("tapa_baul[]"),
            "guardabarro_der_tra_seleccionado": request.POST.getlist("guardafango_der[]"),
            "puerta_trasera_der_seleccionado": request.POST.getlist("puerta_trasera_der[]"),
            "estribo_der_seleccionado": request.POST.getlist("estribo_der[]"),
            "puerta_del_der_seleccionado": request.POST.getlist("puerta_de_der[]"),
            "guardabarro_del_der": request.POST.getlist("guardabarro_del_der[]"),
            "costado_der_seleccionado": request.POST.getlist("costado_der[]"),
            "capota_seleccionado": request.POST.getlist("capota[]"),
            "costado_izq_seleccionado": request.POST.getlist("costado_izq[]"),
            "alma_bomper_del_seleccionado": request.POST.getlist("alma_bomper_del[]"),
            
            #Chasis
            "punta_chasis_del_seleccionado": request.POST.getlist("punta_chasis_del[]"),
            "traviesa_superior_seleccionado": request.POST.getlist("traviesa_superior[]"),
            "polvo_met_del_der_seleccionado": request.POST.getlist("polvo_met_del_der[]"),
            "paral_pano_der_seleccionado": request.POST.getlist("paral_pano_der[]"),
            "paral_pta_der_seleccionado": request.POST.getlist("paral_pta_der[]"),
            "paral_cent_der_seleccionado": request.POST.getlist("paral_cent_der[]"),
            "larguero_capota_der_seleccionado": request.POST.getlist("larguero_capota_der[]"),
            "panel_tra_seleccionado": request.POST.getlist("panel_tra[]"),
            "g_polvo_met_tra_der_seleccionado": request.POST.getlist("g_polvo_met_tra_der[]"),
            "piso_carroceria_seleccionado": request.POST.getlist("piso_carroceria[]"),
            "refuerzo_piso_izq_seleccionado": request.POST.getlist("refuerzo_piso_izq[]"),
            "punta_tra_izq_seleccionado": request.POST.getlist("punta_tra_izq[]"),
            "punta_chasis_del_izq_seleccionado": request.POST.getlist("punta_chasis_del_izq[]"),
            "traviesa_inferior_seleccionado": request.POST.getlist("traviesa_inferior[]"),
            "polvo_met_del_izq_seleccionado": request.POST.getlist("polvo_met_del_izq[]"),
            "paral_pano_izq_seleccionado": request.POST.getlist("paral_pano_izq[]"),
            "paral_pta_izq_seleccionado": request.POST.getlist("paral_pta_izq[]"),
            "paral_cent_izq_seleccionado": request.POST.getlist("paral_cent_izq[]"),
            "larguero_capota_izq_seleccionado": request.POST.getlist("larguero_capota_izq[]"),
            "piso_baul_platon_seleccionado": request.POST.getlist("piso_baul_platon[]"),
            "g_polvo_met_tra_izq_seleccionado": request.POST.getlist("g_polvo_met_tra_izq[]"),
            "punta_tra_der_seleccionado": request.POST.getlist("punta_tra_der[]"),
            "cuna_motor_seleccionado": request.POST.getlist("cuna_motor[]"),
            "rechazado_datos_chasis": request.POST.get('rechazado_datos_chasis'),

            #Interior Cabina
            "carteras_seleccionado": request.POST.getlist("carteras[]"),
            "consola_seleccionado": request.POST.getlist("consola[]"),
            "funcionamiento_sillas_seleccionado": request.POST.getlist("funcionamiento_sillas[]"),
            "millare_seleccionado": request.POST.getlist("millare[]"),
            "persiana_seleccionado": request.POST.getlist("persiana[]"),
            "tapiceria_sillas_seleccionado": request.POST.getlist("tapiceria_sillas[]"),
            "timon_seleccionado": request.POST.getlist("timon[]"),
            "cinturones_seleccionado": request.POST.getlist("cinturones[]"),
            "espejo_interior_seleccionado": request.POST.getlist("espejo_interior[]"),
            "guantera_seleccionado": request.POST.getlist("guantera[]"),
            "parasol_seleccionado": request.POST.getlist("parasol[]"),
            "tapiceria_piso_seleccionado": request.POST.getlist("tapiceria_piso[]"),
            "tapiceria_techo_seleccionado": request.POST.getlist("tapiceria_techo[]"),

            #Sistema Electrico
            "a_ac": request.POST.get("a_ac"),
            "nota_a_ac": request.POST.get("nota_a_ac"),
            "calefaccion": request.POST.get("calefaccion"),
            "nota_calefaccion": request.POST.get("nota_calefaccion"),
            "encendido": request.POST.get("encendido"),
            "nota_encendido": request.POST.get("nota_encendido"),
            "plumillas": request.POST.get("plumillas"),
            "nota_plumillas": request.POST.get("nota_plumillas"),
            "sillas_elect": request.POST.get("sillas_elect"),
            "nota_sillas_elect": request.POST.get("nota_sillas_elect"),
            "bqueo_central": request.POST.get("bqueo_central"),
            "nota_bqueo_central": request.POST.get("nota_bqueo_central"),
            "e_vidrios_elect": request.POST.get("e_vidrios_elect"),
            "nota_e_vidrios_elect": request.POST.get("nota_e_vidrios_elect"),
            "espejos_elect": request.POST.get("espejos_elect"),
            "nota_espejos_elect": request.POST.get("nota_espejos_elect"),
            "radio": request.POST.get("radio"),
            "nota_radio": request.POST.get("nota_radio"),
            "sunroof": request.POST.get("sunroof"),
            "nota_sunroof": request.POST.get("nota_sunroof"),
            "rechazado_datos_sis": request.POST.get('rechazado_datos_sis'),

            #Luces
            "altas": request.POST.get("altas"),
            "nota_altas": request.POST.get("nota_altas"),
            "cocuyos": request.POST.get("cocuyos"),
            "nota_cocuyos": request.POST.get("nota_cocuyos"),
            "reversa": request.POST.get("reversa"),
            "nota_reversa": request.POST.get("nota_reversa"),
            "reversa": request.POST.get("reversa"),
            "nota_reversa": request.POST.get("nota_reversa"),
            "direccionales": request.POST.get("direccionales"),
            "nota_direccionales": request.POST.get("nota_direccionales"),
            "luz_techo": request.POST.get("luz_techo"),
            "nota_luz_techo": request.POST.get("nota_luz_techo"),
            "tercer_stop_luz": request.POST.get("tercer_stop_luz"),
            "nota_tercer_stop_luz": request.POST.get("nota_tercer_stop_luz"),
            "luces_laterales": request.POST.get("luces_laterales"),
            "nota_luces_laterales": request.POST.get("nota_luces_laterales"),
            "bajas": request.POST.get("bajas"),
            "nota_bajas": request.POST.get("nota_bajas"),
            "freno": request.POST.get("freno"),
            "nota_freno": request.POST.get("nota_freno"),
            "estacionarias": request.POST.get("estacionarias"),
            "nota_estacionarias": request.POST.get("nota_estacionarias"),
            "placa": request.POST.get("placa"),
            "nota_placa": request.POST.get("nota_placa"),
            "exploradoras_luz": request.POST.get("exploradoras_luz"),
            "nota_exploradoras_luz": request.POST.get("nota_exploradoras_luz"),
            "antinieblas": request.POST.get("antinieblas"),
            "nota_antinieblas": request.POST.get("nota_antinieblas"),
            "rechazado_datos_luces": request.POST.get('rechazado_datos_luces'),

            #Vidrios
            "panoramico_del": request.POST.getlist("panoramico_del[]"),
            "farola_der": request.POST.getlist("farola_der[]"),
            "farola_izq": request.POST.getlist("farola_izq[]"),
            "exploradoras": request.POST.getlist("exploradoras[]"),
            "antiniebla": request.POST.getlist("antiniebla[]"),
            "espejo_izq": request.POST.getlist("espejo_izq[]"),
            "espejo_der": request.POST.getlist("espejo_der[]"),
            "vidrios_del_izq": request.POST.getlist("vidrios_del_izq[]"),
            "vidrios_tra_izq": request.POST.getlist("vidrios_tra_izq[]"),
            "stop_izq": request.POST.getlist("stop_izq[]"),
            "stop_der": request.POST.getlist("stop_der[]"),
            "tercer_stop": request.POST.getlist("tercer_stop[]"),
            "panoramico_tra": request.POST.getlist("panoramico_tra[]"),
            "vidrios_custodios": request.POST.getlist("vidrios_custodios[]"),
            "vidrios_tra_der": request.POST.getlist("vidrios_tra_der[]"),
            "vidrios_del_der": request.POST.getlist("vidrios_del_der[]"),
            "rechazado_datos_vidrios": request.POST.get('rechazado_datos_vidrios'),
            
            #Llantas
            "llantas_del_izq": request.POST.get("llantas_del_izq"),
            "llantas_del_izq_nota": request.POST.get("llantas_del_izq_nota"),
            "llantas_tra_izq": request.POST.get("llantas_tra_izq"),
            "llantas_tra_izq_nota": request.POST.get("llantas_tra_izq_nota"),
            "llantas_del_der": request.POST.get("llantas_del_der"),
            "llantas_del_der_nota": request.POST.get("llantas_del_der_nota"),
            "llantas_tra_der": request.POST.get("llantas_tra_der"),
            "llantas_tra_der_nota": request.POST.get("llantas_tra_der_nota"),
            "llanta_reemplazo": request.POST.get("llanta_reemplazo"),
            "llanta_reemplazo_nota": request.POST.get("llanta_reemplazo_nota"),
            "rechazado_datos_llantas": request.POST.get('rechazado_datos_llantas'),

            #Fugas
            "aceite_de_motor_datos": request.POST.get("aceite_de_motor_datos"),
            "aceite_de_caja_datos": request.POST.get("aceite_de_caja_datos"),
            "liquido_de_frenos_datos": request.POST.get("liquido_de_frenos_datos"),
            "amortiguadores_delanteros_datos": request.POST.get("amortiguadores_delanteros_datos"),
            "aceite_hidraulicos_datos": request.POST.get("aceite_hidraulicos_datos"),
            "refrigerante_datos": request.POST.get("refrigerante_datos"),
            "compresor_aa_datos": request.POST.get("compresor_aa_datos"),
            "amortiguadores_traseros_datos": request.POST.get("amortiguadores_traseros_datos"),
            "juntas_homocineticas_datos": request.POST.get("juntas_homocineticas_datos"),
            "rechazado_datos_fugas": request.POST.get("rechazado_datos_fugas"),

            #Niveles
            "aceite_motor_niveles": request.POST.get("aceite_motor_niveles"),
            "aceite_hidraulico_niveles": request.POST.get("aceite_hidraulico_niveles"),
            "lavaparabrisas_datos": request.POST.get("lavaparabrisas_datos"),
            "refrigerante_niveles": request.POST.get("refrigerante_niveles"),
            "liquido_frenos_datos": request.POST.get("liquido_frenos_datos"),
            "rechazado_datos_niveles": request.POST.get("rechazado_datos_niveles"),

            #Testigos
            "check_engine_datos": request.POST.get("check_engine_datos"),
            "testigo_abs_datos": request.POST.get("testigo_abs_datos"),
            "control_traccion_datos": request.POST.get("control_traccion_datos"),
            "testigo_airbag_datos": request.POST.get("testigo_airbag_datos"),
            "testigo_alerta_frenos": request.POST.get("testigo_alerta_frenos"),
            "rechazado_testigos": request.POST.get("rechazado_testigos"),

            #Rechazos
            "rechazado_politicas": request.POST.get("rechazado_politicas"),


            #Observaciones
            "comentario": request.POST.get("comentario", "").strip(),

            #Perito
            'perito': request.POST.get('perito'),
        }
        
        
        datos['imagenes_rutas'] = procesar_y_guardar_imagenes(request)

        datos['accesorios'] = accesorios
        
        # Cargar la plantilla con los datos
        template = get_template('pdf_template.html')
        html = template.render(datos)

        # Ruta absoluta al CSS
        css_path = finders.find('css/formato.css')

        # Generar PDF con estilos
        pdf_file = HTML(string=html, base_url=request.build_absolute_uri()).write_pdf(
            stylesheets=[CSS(filename=css_path)]
        )

        # Retornar el PDF
        response = HttpResponse(pdf_file, content_type='application/pdf')
        response['Content-Disposition'] = 'filename="reporte.pdf"'
        return response

    else:
        return render(request, 'formulario.html')

def procesar_y_guardar_imagenes(request):
    imagenes_rutas = []

    for imagen in request.FILES.getlist('imagenes[]'):
        # Abrir imagen
        img = Image.open(imagen)

        # Convertir a RGB si no lo está
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")

        # Redimensionar si es muy grande
        max_ancho = 1024
        if img.width > max_ancho:
            proporcion = max_ancho / float(img.width)
            nuevo_alto = int(float(img.height) * proporcion)
            img = img.resize((max_ancho, nuevo_alto), ImageResampling.LANCZOS)

        # Comprimir y guardar como JPEG
        buffer = BytesIO()
        img.save(buffer, format='JPEG', quality=70, optimize=True)
        buffer.seek(0)

        # Crear nombre y ruta
        nombre_archivo = os.path.splitext(imagen.name)[0] + "_comprimida.jpg"
        ruta_absoluta = os.path.join(settings.MEDIA_ROOT, nombre_archivo)

        with open(ruta_absoluta, 'wb') as f:
            f.write(buffer.read())

        # Agregar la URL accesible
        imagen_url = request.build_absolute_uri(f"{settings.MEDIA_URL}{nombre_archivo}")
        imagenes_rutas.append(imagen_url)

    return imagenes_rutas
