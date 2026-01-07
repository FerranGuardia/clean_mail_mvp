const HowItWorks = () => {
  const steps = [
    {
      step: 1,
      title: "Conecta tu Gmail",
      description: "Inicia sesión de forma segura con tu cuenta de Google. No almacenamos tus datos.",
      icon: "🔐"
    },
    {
      step: 2,
      title: "Configuración Automática",
      description: "Nuestras 15 reglas profesionales se activan automáticamente organizando tus emails.",
      icon: "⚙️"
    },
    {
      step: 3,
      title: "Bandeja Profesional",
      description: "Tu Gmail queda limpio y organizado. Todas las facturas perfectamente rastreadas.",
      icon: "✅"
    }
  ]

  return (
    <div className="py-24 bg-white">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-16">
          <h2 className="text-3xl sm:text-4xl font-bold text-gray-900 mb-4">
            Cómo Funciona
          </h2>
          <p className="text-xl text-gray-600 max-w-3xl mx-auto">
            Tres pasos simples para mantener tu email profesional y nunca perder una factura importante.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          {steps.map((step, index) => (
            <div key={index} className="text-center">
              <div className="relative">
                {/* Step number */}
                <div className="w-16 h-16 bg-blue-600 text-white rounded-full flex items-center justify-center text-xl font-bold mx-auto mb-6">
                  {step.step}
                </div>

                {/* Connecting line (hidden on mobile, visible on md+) */}
                {index < steps.length - 1 && (
                  <div className="hidden md:block absolute top-8 left-full w-full h-0.5 bg-gray-300 -z-10" style={{width: 'calc(100vw / 3)'}}></div>
                )}

                {/* Icon */}
                <div className="text-4xl mb-4">{step.icon}</div>

                {/* Content */}
                <h3 className="text-xl font-semibold text-gray-900 mb-3">{step.title}</h3>
                <p className="text-gray-600">{step.description}</p>
              </div>
            </div>
          ))}
        </div>

        {/* CTA Section */}
        <div className="text-center mt-16">
          <div className="bg-blue-50 rounded-2xl p-8 max-w-2xl mx-auto">
            <h3 className="text-2xl font-bold text-gray-900 mb-4">
              ¿Listo para Gmail Profesional?
            </h3>
            <p className="text-gray-600 mb-6">
              Únete a profesionales que mantienen su bandeja organizada y nunca pierden facturas importantes.
            </p>
            <button className="bg-blue-600 text-white px-8 py-3 rounded-lg text-lg font-semibold hover:bg-blue-700 transition-colors shadow-lg hover:shadow-xl">
              Comenzar Ahora - Gratis
            </button>
          </div>
        </div>
      </div>
    </div>
  )
}

export default HowItWorks
