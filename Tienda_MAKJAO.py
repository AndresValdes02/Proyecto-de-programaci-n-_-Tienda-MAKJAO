from PySide6.QtWidgets import (
    QMainWindow, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QFormLayout, QMessageBox, QHBoxLayout, QApplication,
    QStyle, QGroupBox, QSpinBox, QScrollArea, QSizePolicy)
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QPixmap
import sys

import os
import datetime
from pathlib import Path

os.system("cls")
def absPath(file):
    return str(Path(__file__).parent.absolute() / file)

usuarios = {}
usuario_actual = None  #Variable temporal para guardar el usuario

#Ventana principal
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon(absPath("objetos/logo.png")))
        self.setWindowTitle("Tienda MAKJAO")
        self.setGeometry(200, 200, 600, 500)
        self.setup_ui()

    def setup_ui(self):
        central = QWidget()
        layout = QVBoxLayout()
        
        # Título
        titulo = QLabel("Tienda MAKJAO")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("font-size: 40px; font-weight: bold; margin: 5px 0;")
        layout.addWidget(titulo)
        
        # Subtitulo
        subTitulo = QLabel("¡Tecnología a tu alcance!")
        subTitulo.setAlignment(Qt.AlignCenter)
        subTitulo.setStyleSheet("font-size: 24px; font-weight: bold; margin: 0px 0;")
        layout.addWidget(subTitulo)

        # imagen
        logo = QLabel()
        pixmap = QPixmap(absPath("logo.png")).scaled(150, 150, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        logo.setPixmap(pixmap)
        logo.setAlignment(Qt.AlignCenter)
        layout.addWidget(logo)

        # Botón para ver productos (sin necesidad de cuenta)
        style = QApplication.style()
        btn_productos = QPushButton("Ver productos")
        btn_productos.setIcon(style.standardIcon(QStyle.SP_ComputerIcon))
        btn_productos.clicked.connect(self.abrir_pedido)
        layout.addWidget(btn_productos)
        
        btnAcerca=QPushButton("Información")
        btnAcerca.setIcon(style.standardIcon(QStyle.SP_MessageBoxInformation)) #Icono del botón información
        layout.addWidget(btnAcerca)
        btnAcerca.clicked.connect(self.Acerca_de)
        
        boton_salir = QPushButton("Salir del programa")
        boton_salir.setIcon(style.standardIcon(QStyle.SP_TitleBarCloseButton))
        layout.addWidget(boton_salir)
        boton_salir.clicked.connect(self.salir_aplicacion)
        
        layout.addStretch()
        
        central.setLayout(layout)
        self.setCentralWidget(central)
        
    def salir_aplicacion(self):
        print("Se ha cerrado el")
        # Salir completamente de la aplicación
        QApplication.quit()
    
    #Método para el botón información
    def Acerca_de(self):
        print(f"Se presiono el botón de información" )
        dlg = QMessageBox.about(self, "Acerca de", "<p>Información del programa - Tienda MAKJAO</p><p>Version 1,0 </p>" + 
                                "Autores: <p>Andrés Orlando Valdés Martínez </p><p>Karol Janelly Moreno Quiñones</p><p>María Alejandra Estupiñan Angulo</p>"+
                                "Universidad de Nariño - 2024"
                                "<p>Profesor: Carlos fuel</p>"
                                "")
    #Método para "ver productos"
    def abrir_pedido(self):
        print(f"Se presiono el botón para visualizar los productos" )
        self.hide()
        self.ventana_pedido = VentanaPedido(self)
        self.ventana_pedido.show()
#Ventana donde están los productos
class VentanaPedido(QMainWindow):
    def __init__(self, ventana_padre=None):
        super().__init__()
        self.ventana_padre = ventana_padre
        self.setWindowTitle("Selecciona tus productos")
        self.setWindowIcon(QIcon(absPath("objetos/logo.png")))
        self.setGeometry(100, 100, 800, 600)
        self.carrito = []
        self.setup_ui() 
    def setup_ui(self):
        self.setWindowIcon(QIcon(absPath("objetos/logo.png"))) #logo
        central = QWidget()
        main_layout = QVBoxLayout()
        
        imagen_superior = QLabel()
        pixmap = QPixmap(absPath("objetos/Pro01.png")).scaledToWidth(700, Qt.SmoothTransformation) #imagen de la promoción
        imagen_superior.setPixmap(pixmap)
        imagen_superior.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(imagen_superior)
            
        titulo = QLabel("¡Bienvenido a MAKJAO!") #Titulo principal
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("font-size: 20px; font-weight: bold; margin: 10px 0;")
        main_layout.addWidget(titulo)

        # Area desplazable para los productos
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True) #Ajusta el contenido dentro del area visible disponible.
        scroll_content = QWidget()
        scroll_layout = QVBoxLayout(scroll_content)

        #Productos organizados por categorías
        self.productos = {
            "Audífonos": [
                {"nombre": "Audífonos Sony", "precio": 79999, "imagen": absPath("auriculares/au01.jpg"), "categoria": "Audífonos"},
                {"nombre": "Audífonos JBL", "precio": 89000, "imagen": absPath("auriculares/au02.jpg"), "categoria": "Audífonos"},
                {"nombre": "Audífonos Xiaomi", "precio": 55000, "imagen": absPath("auriculares/au03.jpg"), "categoria": "Audífonos"},
                {"nombre": "Audífonos Samsung", "precio": 99000, "imagen": absPath("auriculares/au04.jpg"), "categoria": "Audífonos"},
            ],
            "Impresoras": [
                {"nombre": "Impresora Epson 345", "precio": 60000, "imagen": absPath("impresoras/im01.png"), "categoria": "Impresoras"},
                {"nombre": "Impresora a color Epson 545", "precio": 450000, "imagen": absPath("impresoras/im02.png"), "categoria": "Impresoras"},
                {"nombre": "Impresora hp", "precio": 150000, "imagen": absPath("impresoras/im03.jpg"), "categoria": "Impresoras"},
                {"nombre": "Impresora Samsung 345", "precio": 900000, "imagen": absPath("impresoras/im04.png"), "categoria": "Impresoras"},
            ],
            "Memorias USB": [
                {"nombre": "Memoria USB Kingston 64GB 2.0", "precio": 50000, "imagen": absPath("memorias/us01.jpg"), "categoria": "Memorias USB"},
                {"nombre": "Memoria USB Adapta 64GB 2.0 roj", "precio": 60000, "imagen": absPath("memorias/us02.jpg"), "categoria": "Memorias USB"},
                {"nombre": "Memoria USB de 16 GB, negra", "precio": 23000, "imagen": absPath("memorias/us03.jpg"), "categoria": "Memorias USB"},
                {"nombre": "Memoria USB de 32 GB, plateada", "precio": 23000, "imagen": absPath("memorias/us04.png"), "categoria": "Memorias USB"},
            ],
            "Cables": [
                {"nombre": "Cable USB sencillo", "precio": 15000, "imagen": absPath("cables/ca01.jpg"), "categoria": "Cables"},
                {"nombre": "Kit Cables de colores", "precio": 35000, "imagen": absPath("cables/ca02.jpg"), "categoria": "Cables"},
                {"nombre": "Cable USB", "precio": 12000, "imagen": absPath("cables/ca03.jpg"), "categoria": "Cables"},
                {"nombre": "Cable HDMI", "precio": 12000, "imagen": absPath("cables/ca04.jpg"), "categoria": "Cables"},
                {"nombre": "Kit de cables", "precio": 25000, "imagen": absPath("cables/ca05.jpg"), "categoria": "Cables"},
            ]
        }

        #Organizar productos por categoría
        for categoria, productos in self.productos.items():
            # Creamos un grupo para cada categoría
            grupo = QGroupBox(categoria) 
            grupo.setStyleSheet("QGroupBox { font-weight: bold; font-size: 16px; }")
            grupo_layout = QVBoxLayout()
            
            for producto in productos:
                fila = QHBoxLayout()

                # Imagen del producto
                imagen_label = QLabel()
                imagen = producto['imagen']
                pixmap = QPixmap(imagen).scaled(70, 70, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                imagen_label.setPixmap(pixmap)
                imagen_label.setFixedSize(70, 70)

                #Texto del producto
                des_producto = QLabel(f"{producto['nombre']} - ${producto['precio']}")
                des_producto.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
                
                #Selector de cantidad
                cantidad = QSpinBox()
                cantidad.setMinimum(1)
                cantidad.setMaximum(20)
                cantidad.setValue(1)
                cantidad.setFixedWidth(60)
                
                # Botón de agregar
                boton = QPushButton("Agregar")
                boton.clicked.connect(lambda _, p=producto, q=cantidad: self.verificar_autenticacion(p, q))

                fila.addWidget(imagen_label)
                fila.addWidget(des_producto)
                fila.addWidget(QLabel("Cantidad:"))
                fila.addWidget(cantidad)
                fila.addWidget(boton)
                grupo_layout.addLayout(fila)
            
            grupo.setLayout(grupo_layout)
            scroll_layout.addWidget(grupo)

        scroll_content.setLayout(scroll_layout)
        scroll_area.setWidget(scroll_content)
        main_layout.addWidget(scroll_area)
        
        # Botones de acción al final
        botones_layout = QHBoxLayout()
        style = QApplication.style()
        #Botón para confirmar pedido
        btn_confirmar = QPushButton("Confirmar pedido")
        btn_confirmar.setIcon(style.standardIcon(QStyle.SP_DialogApplyButton)) #Añadir iconos
        btn_confirmar.clicked.connect(self.confirmar_pedido)
        botones_layout.addWidget(btn_confirmar)
        #Botón para ver los artículos del carrito
        btn_ver_carrito = QPushButton("Ver carrito")
        btn_ver_carrito.setIcon(style.standardIcon(QStyle.SP_FileDialogListView)) #Añadir  (lista)
        btn_ver_carrito.clicked.connect(self.ver_carrito)
        botones_layout.addWidget(btn_ver_carrito)
        #Botón para volver
        btn_volver = QPushButton("Volver")
        btn_volver.setIcon(style.standardIcon(QStyle.SP_ArrowBack))
        btn_volver.clicked.connect(self.volver)
        botones_layout.addWidget(btn_volver)
        
        #Se agregan los botones a la ventana
        main_layout.addLayout(botones_layout)

        central.setLayout(main_layout)
        self.setCentralWidget(central)
    #Método para verificar el usuario 
    def verificar_autenticacion(self, producto, cantidad_spinbox):
        global usuario_actual
        if not usuario_actual: #Verifica si el usuario ha iniciado sesión, sino no lo ha hecho, mostrará un mensaje para que lo haga
            QMessageBox.information(self, "Iniciar sesión", "Debes iniciar sesión o crear una cuenta para agregar productos.")
            self.hide()
            self.ventana_login = VentanaLogin(self, pendiente={"producto": producto, "cantidad": cantidad_spinbox.value()})
            self.ventana_login.show()
        else:
            self.agregar_al_carrito(producto, cantidad_spinbox.value())
    #Método para agregar los productos al carrito
    def agregar_al_carrito(self, producto, cantidad):
        print(f"Se agrego un articulo al carrito" )
        # Revisar si el producto ya está en el carrito
        for item in self.carrito:
            if item['producto']['nombre'] == producto['nombre']:
                item['cantidad'] += cantidad
                QMessageBox.information(self, "Actualizado", 
                                    f"{producto['nombre']} - Nueva cantidad: {item['cantidad']}")
                return
        # Si no está, añadirlo como nuevo
        self.carrito.append({'producto': producto, 'cantidad': cantidad})
        QMessageBox.information(self, "Agregado", 
                            f"{producto['nombre']} - Cantidad: {cantidad} añadido al carrito.")
    #Método para ver los productos del carrito
    def ver_carrito(self):
        print(f"Se abrió el carrito" )
        if not self.carrito: #Revisa si el carrito está vacío
            QMessageBox.information(self, "Carrito Vacío", "No hay productos en tu carrito.")
            return
        #Prepara un resumen y el valor del carrito
        resumen = ""
        total = 0
        
        for item in self.carrito:#Recorre los artículos del carrito y los agrega
            subtotal = item['producto']['precio'] * item['cantidad'] 
            resumen += f"{item['producto']['nombre']} - {item['cantidad']} x ${item['producto']['precio']} = ${subtotal}\n"
            total += subtotal #Va sumando el total de los productos
            
        resumen += f"\nTotal: ${total}"
        
        QMessageBox.information(self, "Tu Carrito", resumen)
    #Método para confirma el pedido
    def confirmar_pedido(self):
        print(f"Se ha confirmado el pedido " )
        global usuario_actual
        if not usuario_actual: #Verifica si el usuario ha iniciado sesión
            QMessageBox.information(self, "Iniciar sesión", "Debes iniciar sesión para confirmar tu pedido.")
            self.hide()
            self.ventana_login = VentanaLogin(self, pendiente="confirmar") #Nos manda a iniciar sesión
            self.ventana_login.show()
            return #sale del método

        if not self.carrito: #Verifica sin el carrito al artículos
            QMessageBox.warning(self, "Vacío", "Tu carrito está vacío.")
            return
        
        total = sum([item['producto']['precio'] * item['cantidad'] for item in self.carrito])
        resumen = "\n".join([f"{item['producto']['nombre']} - {item['cantidad']} x ${item['producto']['precio']} = ${item['producto']['precio'] * item['cantidad']}" 
                        for item in self.carrito])

        QMessageBox.information(self, "Pedido", f"{resumen}\n\nTotal: ${total}")
        self.generar_factura(resumen, total) #Envía el pedido al método para generar factura
    
    def generar_factura(self, resumen, total):
        print(f"Se ha generado la factura" )
        global usuario_actual
        fecha = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S") #fecha y hora de la factura
        nombre_archivo = f"factura_{usuario_actual['nombre'].replace(' ', '_')}_{fecha}.txt" #crea la factura con el nombre del usuario
    
    #Agrega los datos del cliente, el resumen del carrito y el total
        try:
            with open(nombre_archivo, "w", encoding="utf-8") as f:
                f.write("----- FACTURA TIENDA MAKJAO -----\n")
                f.write(f"Cliente: {usuario_actual['nombre']}\n")
                f.write(f"Teléfono: {usuario_actual['telefono']}\n")
                f.write(f"Correo: {usuario_actual['correo']}\n")
                f.write(f"Fecha: {fecha}\n\n")
                f.write("Productos seleccionados:\n")
                f.write(resumen)
                f.write(f"\n\nTOTAL: ${total}\n")
                f.write("Gracias por su compra.\n")
            QMessageBox.information(self, "Factura generada", f"Se guardó: {nombre_archivo}")
            # Limpiamos el carrito después de generar la factura
            self.carrito = []
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo generar la factura: {e}")
    
    def volver(self):
        # Volver a la ventana principal
        if self.ventana_padre:
            self.close()
            self.ventana_padre.show()
    
    def salir_aplicacion(self):
        print(f"Se ha salido de la aplicación" )
        # Salir completamente de la aplicación
        QApplication.quit()
    
    def closeEvent(self, event):
        # Al cerrar esta ventana, mostrar la ventana principal si existe
        if self.ventana_padre:
            self.ventana_padre.show()
        event.accept()

class VentanaLogin(QMainWindow):
    def __init__(self, ventana_padre=None, pendiente=None):
        super().__init__()
        self.setWindowIcon(QIcon(absPath("objetos/logo.png")))
        self.ventana_padre = ventana_padre
        self.setWindowTitle("Iniciar Sesión")
        self.setGeometry(200, 200, 400, 250)
        self.pendiente = pendiente  # producto o "confirmar"
        self.setup_ui()
    def setup_ui(self):
        self.setWindowIcon(QIcon(absPath("objetos/logo.png")))
        central = QWidget()
        layout = QVBoxLayout()
        form = QFormLayout()
        self.correo = QLineEdit()
        self.contrasena = QLineEdit()
        self.contrasena.setEchoMode(QLineEdit.Password)

        form.addRow("Correo:", self.correo)
        form.addRow("Contraseña:", self.contrasena)
        layout.addLayout(form)

        btn_login = QPushButton("Iniciar sesión")
        btn_login.clicked.connect(self.verificar_login)
        layout.addWidget(btn_login)

        btn_registrar = QPushButton("Crear cuenta")
        btn_registrar.clicked.connect(self.abrir_registro)
        layout.addWidget(btn_registrar)
        
        # Botón para volver
        botones_layout = QHBoxLayout()
        style = QApplication.style()
        btn_volver = QPushButton("Volver")
        btn_volver.setIcon(style.standardIcon(QStyle.SP_TitleBarCloseButton))
        btn_volver.clicked.connect(self.volver)
        botones_layout.addWidget(btn_volver)
        
        layout.addLayout(botones_layout)

        central.setLayout(layout)
        self.setCentralWidget(central)

    def verificar_login(self):
        global usuario_actual
        correo = self.correo.text().strip()
        contrasena = self.contrasena.text().strip()

        if correo in usuarios and usuarios[correo]["contrasena"] == contrasena:
            usuario_actual = usuarios[correo]
            usuario_actual["correo"] = correo
            QMessageBox.information(self, "Bienvenido", f"Hola {usuario_actual['nombre']}!")

            self.close()
            self.volver_a_pedido()
        else:
            QMessageBox.critical(self, "Error", "Correo o contraseña incorrectos.")

    def abrir_registro(self):
        self.close()
        self.ventana_registro = VentanaCrearCuenta(self.ventana_padre, pendiente=self.pendiente)
        self.ventana_registro.show()

    def volver_a_pedido(self):
        if self.ventana_padre:
            if isinstance(self.pendiente, dict) and 'producto' in self.pendiente:
                self.ventana_padre.agregar_al_carrito(self.pendiente['producto'], self.pendiente['cantidad'])
            self.ventana_padre.show()
        else:
            self.ventana_pedido = VentanaPedido()
            if isinstance(self.pendiente, dict) and 'producto' in self.pendiente:
                self.ventana_pedido.agregar_al_carrito(self.pendiente['producto'], self.pendiente['cantidad'])
            self.ventana_pedido.show()
    
    def volver(self):
        # Volver a la ventana anterior
        if self.ventana_padre:
            self.close()
            self.ventana_padre.show()
        else:
            self.close()
            ventana = MainWindow()
            ventana.show()
    
    def salir_aplicacion(self):
        # Salir completamente de la aplicación
        QApplication.quit()
    
    def closeEvent(self, event):
        # Al cerrar esta ventana, mostrar la ventana padre si existe
        if self.ventana_padre:
            self.ventana_padre.show()
        event.accept()

class VentanaCrearCuenta(QMainWindow):
    def __init__(self, ventana_padre=None, pendiente=None):
        super().__init__()
        self.ventana_padre = ventana_padre
        self.setWindowTitle("Crear Cuenta")
        self.setWindowIcon(QIcon(absPath("objetos/logo.png")))
        self.setGeometry(200, 200, 400, 300)
        self.pendiente = pendiente
        self.setup_ui()

    def setup_ui(self):
        central = QWidget()
        layout = QVBoxLayout()
        layout = QVBoxLayout()

        #Imagen de inicio se sesión
        imagen= QLabel()
        pixmap = QPixmap("objetos/inicio01.jpg").scaled(150, 150, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        imagen.setPixmap(pixmap)
        imagen.setAlignment(Qt.AlignCenter)
        layout.addWidget(imagen)

        form = QFormLayout()
        self.nombre = QLineEdit()
        self.telefono = QLineEdit()
        self.correo = QLineEdit()
        self.contrasena = QLineEdit()
        self.contrasena.setEchoMode(QLineEdit.Password)
        #Formulario para agregar los datos del usuario 
        form.addRow("Nombre:", self.nombre)
        form.addRow("Teléfono:", self.telefono)
        form.addRow("Correo:", self.correo)
        form.addRow("Contraseña:", self.contrasena)
        layout.addLayout(form)

        btn_crear = QPushButton("Crear cuenta")
        btn_crear.clicked.connect(self.crear_cuenta)
        layout.addWidget(btn_crear)
        
        # Botones para volver y salir
        botones_layout = QHBoxLayout()
        
        btn_volver = QPushButton("Volver")
        btn_volver.clicked.connect(self.volver)
        botones_layout.addWidget(btn_volver)
        
        btn_salir = QPushButton("Salir")
        btn_salir.clicked.connect(self.salir_aplicacion)
        botones_layout.addWidget(btn_salir)
        
        layout.addLayout(botones_layout)
        central.setLayout(layout)
        self.setCentralWidget(central)
        
    def salir_aplicacion(self):
        print("Se ha cerrado el")
        # Salir completamente de la aplicación
        QApplication.quit()
    def crear_cuenta(self):
        global usuario_actual
        nombre = self.nombre.text().strip()
        telefono = self.telefono.text().strip()
        correo = self.correo.text().strip()
        contrasena = self.contrasena.text().strip()
        if not (nombre and telefono and correo and contrasena):
            QMessageBox.warning(self, "Faltan datos", "Completa todos los campos.")
            return
        if correo in usuarios:
            QMessageBox.warning(self, "Ya existe", "Este correo ya fue registrado.")
            return
        usuarios[correo] = {
            "nombre": nombre,
            "telefono": telefono,
            "contrasena": contrasena
        }
        usuario_actual = usuarios[correo]
        usuario_actual["correo"] = correo
        QMessageBox.information(self, "Éxito", "Cuenta creada exitosamente.")
        self.close()
        self.volver_a_pedido()
    def volver_a_pedido(self):
        if self.ventana_padre:
            if isinstance(self.pendiente, dict) and 'producto' in self.pendiente:
                self.ventana_padre.agregar_al_carrito(self.pendiente['producto'], self.pendiente['cantidad'])
            self.ventana_padre.show()
        else:
            self.ventana_pedido = VentanaPedido()
            if isinstance(self.pendiente, dict) and 'producto' in self.pendiente:
                self.ventana_pedido.agregar_al_carrito(self.pendiente['producto'], self.pendiente['cantidad'])
            self.ventana_pedido.show()
    def volver(self):
        # Volver a la ventana anterior
        self.close()
        ventana_login = VentanaLogin(self.ventana_padre, self.pendiente)
        ventana_login.show()
    
    def closeEvent(self, event):
        # Al cerrar esta ventana, mostrar la ventana de login
        ventana_login = VentanaLogin(self.ventana_padre, self.pendiente)
        ventana_login.show()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    #Estilo
    style_sheet = """
    * {
        font-family: 'JetBrains Mono', 'Fira Code', 'SF Mono', monospace;
        font-size: 14px;
    }
    QWidget {
        background-color: #1E1E2E;
        color: #CDD6F4;
    }
    QLabel {
        font-size: 18px;
        font-weight: 600;
        color: #89B4FA;
        padding: 10px;
        letter-spacing: 0.5px;
    }
    QPushButton {
        background-color: #313244;
        color: #F5E0DC;
        border: 1px solid #45475A;
        border-radius: 8px;
        padding: 10px 24px;
        font-weight: 500;
        margin-top: 10px;
        letter-spacing: 0.4px;
    }
    QPushButton:hover {
        background-color: #45475A;
    }
    QPushButton:pressed {
        background-color: #585B70;
    }
    QToolTip {
        background-color: #181825;
        color: #A6ADC8;
        padding: 6px;
        border-radius: 5px;
        border: 1px solid #89B4FA;
    }
    QLineEdit, QPlainTextEdit, QTextEdit, QComboBox {
        background-color: #313244;
        color: #F5E0DC;
        border: 1px solid #45475A;
        border-radius: 6px;
        padding: 6px;
    }
    """
    app.setStyleSheet(style_sheet)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
