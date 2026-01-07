const Process = () => {
  const processingSteps = [
    {
      step: 1,
      title: "Conectar Gmail",
      description: "CleanMail accede a tu Gmail de forma segura mediante OAuth 2.0",
      icon: "🔐"
    },
    {
      step: 2,
      title: "Analizar Correos",
      description: "Revisa automáticamente tus emails sin leer aplicando las reglas profesionales",
      icon: "🔍"
    },
    {
      step: 3,
      title: "Etiquetar Automáticamente",
      description: "Los emails se organizan en categorías: Bills, Orders, Trash, Social, Technical",
      icon: "🏷️"
    },
    {
      step: 4,
      title: "Mantener Profesional",
      description: "Tu bandeja queda limpia y organizada, con todas las facturas bien rastreadas",
      icon: "✅"
    }
  ]

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-3xl font-bold text-gray-900">Procesar Emails Profesionalmente</h1>
        <p className="text-gray-600 mt-2">Mantén tu Gmail profesional y nunca pierdas una factura importante</p>
      </div>

      <div className="bg-emerald-50 border border-emerald-200 rounded-lg p-6">
        <h3 className="text-lg font-medium text-emerald-900 mb-2">💼 Enfoque Profesional</h3>
        <p className="text-emerald-800">
          CleanMail está diseñado específicamente para mantener tu bandeja de entrada profesional,
          eliminando correos no deseados y asegurando que todas tus facturas y pedidos estén
          perfectamente organizados y etiquetados.
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {processingSteps.map((step) => (
          <div key={step.step} className="bg-white p-6 rounded-lg shadow border">
            <div className="flex items-center mb-4">
              <div className="flex-shrink-0 w-8 h-8 bg-blue-600 text-white rounded-full flex items-center justify-center font-bold text-sm mr-3">
                {step.step}
              </div>
              <span className="text-xl mr-3">{step.icon}</span>
              <h3 className="text-lg font-medium text-gray-900">{step.title}</h3>
            </div>
            <p className="text-gray-600">{step.description}</p>
          </div>
        ))}
      </div>

      <div className="bg-white p-8 rounded-lg shadow">
        <h2 className="text-xl font-medium text-gray-900 mb-4 text-center">Categorías Automáticas</h2>
        <div className="grid grid-cols-2 md:grid-cols-5 gap-4">
          <div className="text-center p-4 bg-red-50 rounded-lg border border-red-200">
            <div className="text-2xl mb-2">🗑️</div>
            <div className="font-medium text-red-900">Trash</div>
            <div className="text-xs text-red-700">Promociones, ofertas</div>
          </div>
          <div className="text-center p-4 bg-blue-50 rounded-lg border border-blue-200">
            <div className="text-2xl mb-2">📱</div>
            <div className="font-medium text-blue-900">Social</div>
            <div className="text-xs text-blue-700">Redes sociales</div>
          </div>
          <div className="text-center p-4 bg-green-50 rounded-lg border border-green-200">
            <div className="text-2xl mb-2">📄</div>
            <div className="font-medium text-green-900">Bills</div>
            <div className="text-xs text-green-700">Facturas, recibos</div>
          </div>
          <div className="text-center p-4 bg-purple-50 rounded-lg border border-purple-200">
            <div className="text-2xl mb-2">📦</div>
            <div className="font-medium text-purple-900">Orders</div>
            <div className="text-xs text-purple-700">Pedidos, envíos</div>
          </div>
          <div className="text-center p-4 bg-gray-50 rounded-lg border border-gray-200">
            <div className="text-2xl mb-2">⚙️</div>
            <div className="font-medium text-gray-900">Technical</div>
            <div className="text-xs text-gray-700">Despliegues, alertas</div>
          </div>
        </div>
      </div>

      <div className="bg-yellow-50 border border-yellow-200 rounded-lg p-6">
        <h3 className="text-lg font-medium text-yellow-900 mb-2">⚡ Próximamente</h3>
        <p className="text-yellow-800">
          La interfaz completa para procesar emails estará disponible pronto. Por ahora,
          las reglas automáticas se aplican en segundo plano cuando conectas tu Gmail.
        </p>
      </div>
    </div>
  )
}

export default Process
