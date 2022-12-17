import asyncio

from datetime import datetime
from PyQt5 import QtWidgets, QtGui, QtCore

from .interface import Ui_MainWindow
from .sdk import SigmaCreditSDK
from .utils import retrieve_data
from .entries import PersonaEntry

__version__ = "0.1.0"


class SigmaClient(Ui_MainWindow):
    def __init__(self, mainwindow):
        super().__init__()
        self.mainwindow = mainwindow
        self.setupUi(mainwindow)
        self.__connect_signals()
        self.__bloquear_peticiones()
        self.sigma_version_label.setText(f"Sigma Credits v{__version__}")
        self.mostrar_mensaje(
            self.mconsole_textBrowser,
            f"Iniciando Sigma Credits build v{__version__}",
        )

        self.sdk = None
        self.local_credits = 0.00
        self.personas_cargadas = []

    def __connect_signals(self):
        self.validarLogin_pushButton.clicked.connect(self.validar_login)
        self.buscarPatente_pushButton.clicked.connect(self.buscar_por_patente)
        self.proBuscarNum_pushButton.clicked.connect(
            self.buscar_datos_por_numero
        )
        self.proBuscarDni_pushButton.clicked.connect(
            self.buscar_datos_profesional
        )

        self.proBuscarNombre_pushButton.clicked.connect(
            self.buscar_personas_nombre
        )

        self.proBuscarVecinos_pushButton.clicked.connect(
            self.buscar_vecinos_direccion
        )

        self.p3buscarcvuTitular_pushButton.clicked.connect(
            self.buscar_datos_cbu
        )

        self.p3emailBuscar_pushButton.clicked.connect(self.buscar_datos_email)

        self.p3buscarDato_pushButton.clicked.connect(
            self.buscar_datos_numero_p3
        )

        self.buscarLeaks_pushButton.clicked.connect(self.buscar_data_breach)

    def __bloquear_peticiones(self):
        self.buscarPatente_pushButton.setEnabled(False)
        self.proBuscarNum_pushButton.setEnabled(False)
        self.proBuscarDni_pushButton.setEnabled(False)
        self.proBuscarNombre_pushButton.setEnabled(False)
        self.proBuscarVecinos_pushButton.setEnabled(False)
        self.p3buscarcvuTitular_pushButton.setEnabled(False)
        self.p3emailBuscar_pushButton.setEnabled(False)
        self.p3buscarDato_pushButton.setEnabled(False)
        self.buscarLeaks_pushButton.setEnabled(False)

    def __habilitar_peticiones(self):
        self.buscarPatente_pushButton.setEnabled(True)
        self.proBuscarNum_pushButton.setEnabled(True)
        self.proBuscarDni_pushButton.setEnabled(True)
        self.proBuscarNombre_pushButton.setEnabled(True)
        self.proBuscarVecinos_pushButton.setEnabled(True)
        self.p3buscarcvuTitular_pushButton.setEnabled(True)
        self.p3emailBuscar_pushButton.setEnabled(True)
        self.p3buscarDato_pushButton.setEnabled(True)
        self.buscarLeaks_pushButton.setEnabled(True)

    def __limpiar_tabla(self, tabla):
        while tabla.rowCount() > 0:
            tabla.removeRow(0)

    def mostrar_mensaje(self, consola, msg: str):
        consola.append(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}")

    def update_balance(self, balance: float):
        self.local_credits = balance
        self.MainWindow.setWindowTitle(
            f"Sigma Credits (Balance: ${self.local_credits})"
        )

    async def async_validar_login(self):
        usuario = self.usuario_lineEdit.text().strip()
        clave = self.password_lineEdit.text().strip()
        self.mostrar_mensaje(
            self.mconsole_textBrowser,
            f"Validando credenciales {usuario}:{clave} ...",
        )

        try:
            sdk = await SigmaCreditSDK.from_login(usuario, clave)
        except:
            self.mostrar_mensaje(
                self.mconsole_textBrowser,
                "Las credenciales son invalidas o no es posible logearse en este momento",
            )
            return

        balance_response = await sdk.balance()
        balance = balance_response["creditos"]

        self.mostrar_mensaje(
            self.mconsole_textBrowser,
            f"Bienvenido {usuario}! Dispones de {balance} creditos",
        )
        self.update_balance(balance)
        self.sdk = sdk
        self.mostrar_mensaje(
            self.mconsole_textBrowser,
            f"Tu cliente ha sido configurado para utilizar la token {sdk.token}",
        )
        self.__habilitar_peticiones()

    async def async_buscar_por_patente(self):
        patente_str = self.patenteBuscar_lineEdit.text().strip()
        self.mostrar_mensaje(
            self.patentes_textBrowser,
            f"Buscando registros de la patente {patente_str} ...",
        )

        response = await self.sdk.search_plate(patente_str)

        if "error" in response:
            self.mostrar_mensaje(
                self.patentes_textBrowser, response.get("error")
            )
        else:
            self.mostrar_mensaje(
                self.patentes_textBrowser,
                f"Se encontraron {len(response)} registros relacionados a la patente {patente_str}, cargando ...",
            )
            self.update_balance(self.local_credits - 0.25)
            for registro in response:
                rowPosition = self.patentes_tableWidget.rowCount()
                self.patentes_tableWidget.insertRow(rowPosition)
                for indice, campo in enumerate(
                    [
                        "patente",
                        "documento",
                        "vehiculo",
                        "marca",
                        "anio",
                        "titular",
                        "porcentaje",
                        "calle",
                        "altura",
                        "piso",
                        "depto",
                        "codigo_postal",
                        "localidad",
                        "transferencia",
                    ]
                ):
                    self.patentes_tableWidget.setItem(
                        rowPosition,
                        indice,
                        QtWidgets.QTableWidgetItem(
                            retrieve_data(registro, campo)
                        ),
                    )

    async def async_buscar_datos_por_numero(self):
        numero_str = self.proNumeroBuscar_lineEdit.text().strip()
        self.mostrar_mensaje(
            self.numeros_textBrowser,
            f"Buscando datos relacionados al numero {numero_str} ...",
        )

        response = await self.sdk.search_phone(numero_str)

        if "error" in response:
            self.mostrar_mensaje(
                self.numeros_textBrowser, response.get("error")
            )
        else:
            self.mostrar_mensaje(
                self.numeros_textBrowser,
                f"Se encontraron {len(response)} entidades relacionadas al numero {numero_str}, cargando datos ...",
            )
            self.update_balance(self.local_credits - 0.25)
            for entidad in response:
                rowPosition = self.proNumeros_tableWidget.rowCount()
                self.proNumeros_tableWidget.insertRow(rowPosition)
                for indice, campo in enumerate(
                    [
                        "celular",
                        "documento",
                        "nombre",
                        "direccion",
                        "localidad",
                        "provincia",
                        "codigo_postal",
                        "empresa",
                    ]
                ):
                    self.proNumeros_tableWidget.setItem(
                        rowPosition,
                        indice,
                        QtWidgets.QTableWidgetItem(
                            retrieve_data(entidad, campo)
                        ),
                    )

    async def async_buscar_datos_profesional(self):
        dni_str = self.proDniBuscar_lineEdit.text().strip()
        genero_str = self.proGenero_comboBox.currentText()
        self.mostrar_mensaje(
            self.personas_textBrowser,
            f"Buscando datos relacionados al dni {dni_str} ...",
        )

        response = await self.sdk.search_dni(dni_str, genero_str)

        if "error" in response:
            self.mostrar_mensaje(
                self.personas_textBrowser, response.get("mensaje")
            )
        else:
            self.mostrar_mensaje(
                self.personas_textBrowser,
                f"Se ha encontrado el DNI {dni_str}, cargando datos ...",
            )
            self.update_balance(self.local_credits - 0.25)
            self.proEmision_output_lineEdit.setText(
                retrieve_data(response, "emision")
            )
            self.proNroDoc_output_lineEdit.setText(
                retrieve_data(response, "documento")
            )
            self.proApellido_output_lineEdit.setText(
                retrieve_data(response, "apellido")
            )
            self.proNombre_output_lineEdit.setText(
                retrieve_data(response, "nombres")
            )
            self.proCUIL_output_lineEdit.setText(
                retrieve_data(response, "cuil")
            )
            self.proBarrio_output_lineEdit.setText(
                retrieve_data(response, "barrio")
            )
            self.proCalle_output_lineEdit.setText(
                retrieve_data(response, "calle")
            )
            self.proAltura_output_lineEdit.setText(
                retrieve_data(response, "numero")
            )
            self.proDepartamento_output_lineEdit.setText(
                retrieve_data(response, "departamento")
            )
            self.proPiso_output_lineEdit.setText(
                retrieve_data(response, "piso")
            )
            self.proMonoblock_output_lineEdit.setText(
                retrieve_data(response, "monoblock")
            )
            self.proCiudad_output_lineEdit.setText(
                retrieve_data(response, "ciudad")
            )
            self.proMunicipio_output_lineEdit.setText(
                retrieve_data(response, "municipio")
            )
            self.proProvincia_output_lineEdit.setText(
                retrieve_data(response, "provincia")
            )
            self.proPais_output_lineEdit.setText(
                retrieve_data(response, "pais")
            )

            self.proFechaNacimiento_output_lineEdit.setText(
                retrieve_data(response, "fecha_nacimiento")
            )

            fallecimiento = retrieve_data(response, "fallecido")
            if fallecimiento == "Sin Aviso de Fallecimiento":
                fallecimiento = "No"

            self.proFallecido_output_lineEdit.setText(fallecimiento)

            if type(response.get("cobertura")) == list:
                for obrasocial in response.get("cobertura"):
                    self.obraSocial_output_comboBox.addItem(
                        obrasocial["cobertura"]
                    )
            else:
                self.obraSocial_output_comboBox.clear()

    async def async_buscar_personas_nombre(self):
        nombre_str = self.proNombreBuscar_lineEdit.text().strip()
        provincia_str = self.proProvincia_comboBox.currentText() or None
        localidad_str = self.proLocalidadBuscar_lineEdit.text().strip() or None
        edad_min_str = self.proEdadMin_spinBox.value() or None
        edad_max_str = self.proEdadMax_spinBox.value() or None

        self.mostrar_mensaje(
            self.personas_textBrowser,
            f"Buscando personas con nombre '{nombre_str}' ...",
        )

        response = await self.sdk.search_name(
            nombre_str,
            {
                None: -1,
                "capital_federal": 0,
                "buenos_aires": 1,
                "catamarca": 2,
                "chaco": 16,
                "chubut": 17,
                "cordoba": 3,
                "corrientes": 4,
                "entre_rios": 5,
                "formosa": 18,
                "jujuy": 6,
                "la_pampa": 21,
                "la_rioja": 8,
                "mendoza": 7,
                "misiones": 19,
                "neuquen": 20,
                "rio_negro": 22,
                "salta": 9,
                "san_juan": 10,
                "san_luis": 11,
                "santa_cruz": 23,
                "santa_fe": 12,
                "santiago_del_estero": 13,
                "tierra_del_fuego": 24,
                "tucuman": 14,
            }[provincia_str],
            localidad_str,
            edad_min_str,
            edad_max_str,
        )

        if "error" in response:
            self.mostrar_mensaje(
                self.personas_textBrowser, response.get("error")
            )
        else:
            self.mostrar_mensaje(
                self.personas_textBrowser,
                f"Se encontraron {len(response)} resultados, cargando ...",
            )
            self.update_balance(self.local_credits - 0.25)
            for persona in response:

                entry = PersonaEntry(
                    self.scrollArea,
                    persona["documento"],
                    persona["nombre"],
                    persona["provincia"],
                )
                self.verticalLayout_2.addWidget(entry)
                self.scrollArea.setWidget(self.scrollAreaWidgetContents)
                self.verticalLayout.addWidget(self.scrollArea)
                self.personas_cargadas.append(entry)

    async def async_buscar_vecinos_direccion(self):
        direccion_str = self.proDireccionBuscar_lineEdit.text().strip()
        self.mostrar_mensaje(
            self.personas_textBrowser,
            f"Buscando vecinos en {direccion_str} ...",
        )

        response = await self.sdk.search_address(direccion_str)

        if "error" in response:
            self.mostrar_mensaje(
                self.personas_textBrowser, response.get("error")
            )
        else:
            self.mostrar_mensaje(
                self.personas_textBrowser,
                f"Se encontraron {len(response)} vecinos en {direccion_str}, cargando datos ...",
            )
            self.update_balance(self.local_credits - 0.25)
            for vecino in response:
                rowPosition = self.proVecinos_tableWidget.rowCount()
                self.proVecinos_tableWidget.insertRow(rowPosition)
                for indice, campo in enumerate(
                    [
                        "doc",
                        "nombre",
                        "numero",
                        "empresa",
                        "direccion",
                        "localidad",
                        "provincia",
                        "codigo_postal",
                    ]
                ):
                    self.proVecinos_tableWidget.setItem(
                        rowPosition,
                        indice,
                        QtWidgets.QTableWidgetItem(
                            retrieve_data(vecino, campo)
                        ),
                    )

    async def async_buscar_datos_cbu(self):
        cbv_or_alias_str = self.p3cbvubuscar_lineEdit.text().strip()
        self.mostrar_mensaje(
            self.banking_textBrowser,
            f"Buscando datos del titular de {cbv_or_alias_str} ...",
        )

        response = await self.sdk.search_cbu(cbv_or_alias_str)

        if "error" in response:
            self.mostrar_mensaje(
                self.banking_textBrowser, response.get("mensaje")
            )
        else:
            self.mostrar_mensaje(
                self.banking_textBrowser,
                f"Se encontraron datos del titular de {cbv_or_alias_str}, cargando ...",
            )
            self.update_balance(self.local_credits - 0.25)
            self.p3titular_output_lineEdit.setText(
                retrieve_data(response, "nombre")
            )
            self.p3cuit_output_lineEdit.setText(
                retrieve_data(response, "cuit")
            )
            self.p3banco_output_lineEdit.setText(
                retrieve_data(response, "banco")
            )
            self.p3tipocuenta_output_lineEdit.setText(
                retrieve_data(response, "cuenta_tipo")
            )
            self.p3cbucvu_output_lineEdit.setText(
                retrieve_data(response, "cbu")
            )

    async def async_buscar_datos_email(self):
        email_str = self.p3emailBuscar_lineEdit.text().strip()
        self.mostrar_mensaje(
            self.banking_textBrowser,
            f"Buscando datos de email {email_str} ...",
        )

        response = await self.sdk.search_email(email_str)

        if "error" in response:
            self.mostrar_mensaje(
                self.banking_textBrowser, response.get("error")
            )
        else:
            self.mostrar_mensaje(
                self.banking_textBrowser,
                f"Se encontraron datos del email {email_str}, cargando ...",
            )
            self.update_balance(self.local_credits - 0.25)
            self.p3nombres_output_lineEdit.setText(
                retrieve_data(response, "nombre")
            )
            self.p3apellido_output_lineEdit.setText(
                retrieve_data(response, "apellido")
            )

    async def async_buscar_datos_numero_p3(self):
        numero_str = self.p3numeroBuscar_lineEdit.text().strip()
        self.mostrar_mensaje(
            self.numeros_textBrowser,
            f"Buscando datos del numero {numero_str} ...",
        )

        response = await self.sdk.search_number(numero_str)

        if "error" in response:
            self.mostrar_mensaje(
                self.numeros_textBrowser, response.get("error")
            )
        else:
            self.mostrar_mensaje(
                self.numeros_textBrowser,
                f"Se encontraron datos del numero {numero_str}, cargando ...",
            )
            self.update_balance(self.local_credits - 0.25)
            self.p3nombres2_output_lineEdit.setText(
                retrieve_data(response, "nombre")
            )
            self.p3apellidos2_output_lineEdit.setText(
                retrieve_data(response, "apellido")
            )
            self.p3email_output_lineEdit.setText(
                retrieve_data(response, "email")
            )
            self.p3numero_output_lineEdit.setText(
                retrieve_data(response, "numero")
            )

    async def async_buscar_data_breach(self):
        query_str = self.queryBreach_lineEdit.text().strip()

        self.mostrar_mensaje(
            self.banking_textBrowser,
            f"Buscando query {query_str} en nuestra DB ...",
        )

        response = await self.sdk.search_breach(query_str)

        if "error" in response:
            self.mostrar_mensaje(
                self.banking_textBrowser, response.get("error")
            )
        else:
            self.mostrar_mensaje(
                self.banking_textBrowser,
                f"Se encontraron {len(response)} entradas relacionados a la query {query_str}, cargando ...",
            )
            self.update_balance(self.local_credits - 0.25)
            for entrada in response:
                rowPosition = self.dataBreachResults_tableWidget.rowCount()
                self.dataBreachResults_tableWidget.insertRow(rowPosition)
                for indice, campo in enumerate(
                    [
                        "usuario",
                        "password",
                    ]
                ):
                    self.dataBreachResults_tableWidget.setItem(
                        rowPosition,
                        indice,
                        QtWidgets.QTableWidgetItem(
                            retrieve_data(entrada, campo)
                        ),
                    )

    def validar_login(self):
        self.__bloquear_peticiones()
        if (
            self.usuario_lineEdit.text().strip()
            and self.password_lineEdit.text().strip()
        ):
            asyncio.ensure_future(self.async_validar_login())

    def buscar_por_patente(self):
        self.__limpiar_tabla(self.patentes_tableWidget)
        if self.patenteBuscar_lineEdit.text().strip():
            asyncio.ensure_future(self.async_buscar_por_patente())

    def buscar_datos_por_numero(self):
        self.__limpiar_tabla(self.proNumeros_tableWidget)
        if self.proNumeroBuscar_lineEdit.text().strip():
            asyncio.ensure_future(self.async_buscar_datos_por_numero())

    def buscar_datos_profesional(self):
        if self.proDniBuscar_lineEdit.text().strip():
            asyncio.ensure_future(self.async_buscar_datos_profesional())

    def buscar_personas_nombre(self):
        if self.personas_cargadas:
            while self.verticalLayout_2.count():
                child = self.verticalLayout_2.takeAt(0)
                if child.widget() is not None:
                    child.widget().deleteLater()
            self.personas_cargadas = []
        if self.proNombreBuscar_lineEdit.text().strip():
            asyncio.ensure_future(self.async_buscar_personas_nombre())

    def buscar_vecinos_direccion(self):
        self.__limpiar_tabla(self.proVecinos_tableWidget)
        if self.proDireccionBuscar_lineEdit.text().strip():
            asyncio.ensure_future(self.async_buscar_vecinos_direccion())

    def buscar_datos_cbu(self):
        if self.p3cbvubuscar_lineEdit.text().strip():
            asyncio.ensure_future(self.async_buscar_datos_cbu())

    def buscar_datos_email(self):
        if self.p3emailBuscar_lineEdit.text().strip():
            asyncio.ensure_future(self.async_buscar_datos_email())

    def buscar_datos_numero_p3(self):
        if self.p3numeroBuscar_lineEdit.text().strip():
            asyncio.ensure_future(self.async_buscar_datos_numero_p3())

    def buscar_data_breach(self):
        self.__limpiar_tabla(self.dataBreachResults_tableWidget)
        if self.queryBreach_lineEdit.text().strip():
            asyncio.ensure_future(self.async_buscar_data_breach())
