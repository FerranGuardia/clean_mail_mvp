const Rules = () => {
  const professionalCategories = [
    {
      name: "Bills & Invoices",
      description: "Facturas, recibos, comprobantes de pago",
      icon: "📄",
      examples: ["factura", "invoice", "recibo", "billing"]
    },
    {
      name: "Orders & Shipping",
      description: "Pedidos y notificaciones de envío",
      icon: "📦",
      examples: ["pedido", "order", "enviado", "delivered"]
    },
    {
      name: "Trash & Promotions",
      description: "Promociones, ofertas y correos no deseados",
      icon: "🗑️",
      examples: ["oferta", "promo", "descuento", "newsletter"]
    },
    {
      name: "Social Media",
      description: "Notificaciones de redes sociales",
      icon: "📱",
      examples: ["facebook", "instagram", "twitter", "linkedin"]
    },
    {
      name: "Technical & Deployment",
      description: "Notificaciones técnicas y de despliegue",
      icon: "⚙️",
      examples: ["deploy", "deployment", "build", "alert"]
    }
  ]

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-3xl font-bold text-gray-900">Professional Email Rules</h1>
        <p className="text-gray-600 mt-2">Mantén tu Gmail profesional y rastrea todas tus facturas automáticamente</p>
      </div>

      <div className="bg-blue-50 border border-blue-200 rounded-lg p-6">
        <h3 className="text-lg font-medium text-blue-900 mb-2">🎯 Objetivo Principal</h3>
        <p className="text-blue-800">
          Mantener tu bandeja de entrada profesional eliminando correos no deseados y asegurándote
          de nunca perder facturas importantes o notificaciones de pedidos.
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {professionalCategories.map((category) => (
          <div key={category.name} className="bg-white p-6 rounded-lg shadow border">
            <div className="flex items-center mb-4">
              <span className="text-2xl mr-3">{category.icon}</span>
              <h3 className="text-lg font-medium text-gray-900">{category.name}</h3>
            </div>
            <p className="text-gray-600 mb-4">{category.description}</p>
            <div className="flex flex-wrap gap-2">
              {category.examples.map((example) => (
                <span
                  key={example}
                  className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-gray-100 text-gray-800"
                >
                  {example}
                </span>
              ))}
            </div>
          </div>
        ))}
      </div>

      <div className="bg-white p-8 rounded-lg shadow text-center">
        <h2 className="text-xl font-medium text-gray-900 mb-4">Reglas Automáticas Incluidas</h2>
        <p className="text-gray-600 mb-6">
          CleanMail incluye reglas pre-configuradas para español e inglés que se activan automáticamente
          para mantener tu bandeja profesional.
        </p>
        <div className="bg-green-50 border border-green-200 rounded-md p-4">
          <p className="text-sm text-green-800">
            ✅ Las reglas se aplican automáticamente cuando procesas tus emails
          </p>
        </div>
      </div>
    </div>
  )
}

export default Rules
