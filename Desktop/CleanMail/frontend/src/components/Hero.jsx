import { Link } from 'react-router-dom'

const Hero = () => {
  return (
    <div className="bg-gradient-to-br from-blue-50 to-indigo-100">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-24">
        <div className="text-center">
          <h1 className="text-4xl sm:text-5xl lg:text-6xl font-bold text-gray-900 mb-8">
            Mantén tu Gmail
            <span className="text-blue-600"> Profesional</span>
          </h1>

          <p className="text-xl text-gray-600 mb-8 max-w-3xl mx-auto">
            Nunca pierdas una factura importante. CleanMail organiza automáticamente tu bandeja de entrada,
            eliminando correos no deseados y asegurando que todas tus facturas estén perfectamente rastreadas.
          </p>

          <div className="flex flex-col sm:flex-row gap-4 justify-center items-center mb-12">
            <Link
              to="/app/login"
              className="bg-blue-600 text-white px-8 py-4 rounded-lg text-lg font-semibold hover:bg-blue-700 transition-colors shadow-lg hover:shadow-xl"
            >
              Comenzar Gratis
            </Link>
            <div className="text-sm text-gray-500">
              Sin tarjeta de crédito • Configuración en 2 minutos
            </div>
          </div>

          {/* Key Benefits */}
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8 max-w-4xl mx-auto">
            <div className="bg-white p-6 rounded-xl shadow-sm border border-gray-100">
              <div className="w-12 h-12 bg-green-100 rounded-lg flex items-center justify-center mb-4 mx-auto">
                <span className="text-2xl">📄</span>
              </div>
              <h3 className="text-lg font-semibold text-gray-900 mb-2">Facturas Seguras</h3>
              <p className="text-gray-600 text-sm">Todas tus facturas automáticamente etiquetadas y organizadas</p>
            </div>

            <div className="bg-white p-6 rounded-xl shadow-sm border border-gray-100">
              <div className="w-12 h-12 bg-blue-100 rounded-lg flex items-center justify-center mb-4 mx-auto">
                <span className="text-2xl">🗑️</span>
              </div>
              <h3 className="text-lg font-semibold text-gray-900 mb-2">Bandeja Limpia</h3>
              <p className="text-gray-600 text-sm">Elimina promociones, social y correos no deseados automáticamente</p>
            </div>

            <div className="bg-white p-6 rounded-xl shadow-sm border border-gray-100">
              <div className="w-12 h-12 bg-blue-100 rounded-lg flex items-center justify-center mb-4 mx-auto">
                <span className="text-2xl">⚡</span>
              </div>
              <h3 className="text-lg font-semibold text-gray-900 mb-2">Bilingüe</h3>
              <p className="text-gray-600 text-sm">Funciona perfectamente en español e inglés</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

export default Hero
