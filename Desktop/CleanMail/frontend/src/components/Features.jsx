const Features = () => {
  const features = [
    {
      icon: "📄",
      title: "Rastreo de Facturas",
      description: "Nunca pierdas una factura importante. Detecta automáticamente facturas, recibos y documentos de pago en español e inglés.",
      details: ["Detección automática de PDFs", "Etiquetas profesionales", "Historial completo"]
    },
    {
      icon: "📦",
      title: "Seguimiento de Pedidos",
      description: "Mantén el control de todos tus pedidos y envíos. Desde confirmaciones hasta entregas.",
      details: ["Confirmaciones de pedido", "Notificaciones de envío", "Actualizaciones de entrega"]
    },
    {
      icon: "🗑️",
      title: "Limpieza Automática",
      description: "Elimina automáticamente correos no deseados manteniendo tu bandeja profesional.",
      details: ["Promociones y ofertas", "Notificaciones sociales", "Correos no-reply"]
    },
    {
      icon: "🔒",
      title: "Seguro y Privado",
      description: "Tu privacidad es nuestra prioridad. Acceso seguro mediante OAuth de Google.",
      details: ["Sin almacenamiento de datos", "Encriptación completa", "OAuth 2.0 seguro"]
    },
    {
      icon: "⚡",
      title: "Procesamiento Inteligente",
      description: "Reglas pre-configuradas que funcionan automáticamente en español e inglés.",
      details: ["15 reglas profesionales", "Bilingüe español-inglés", "Actualización automática"]
    },
    {
      icon: "📊",
      title: "Dashboard Profesional",
      description: "Visualiza tu organización de emails con estadísticas claras y útiles.",
      details: ["Facturas rastreadas", "Categorías organizadas", "Historial de actividad"]
    }
  ]

  return (
    <div className="py-24 bg-gray-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-16">
          <h2 className="text-3xl sm:text-4xl font-bold text-gray-900 mb-4">
            Características Profesionales
          </h2>
          <p className="text-xl text-gray-600 max-w-3xl mx-auto">
            Diseñado específicamente para profesionales que necesitan mantener su email organizado
            y nunca perder documentos importantes.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {features.map((feature, index) => (
            <div key={index} className="bg-white p-8 rounded-xl shadow-sm border border-gray-100 hover:shadow-md transition-shadow">
              <div className="text-4xl mb-4">{feature.icon}</div>
              <h3 className="text-xl font-semibold text-gray-900 mb-3">{feature.title}</h3>
              <p className="text-gray-600 mb-4">{feature.description}</p>
              <ul className="space-y-2">
                {feature.details.map((detail, idx) => (
                  <li key={idx} className="text-sm text-gray-500 flex items-center">
                    <span className="w-1.5 h-1.5 bg-blue-600 rounded-full mr-2"></span>
                    {detail}
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </div>
      </div>
    </div>
  )
}

export default Features
