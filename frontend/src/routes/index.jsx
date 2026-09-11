import { Routes, Route, Navigate } from 'react-router-dom'

import Produtos from '../pages/Produtos'
import ProdutoForm from '../pages/ProdutoForm'

function AppRoutes() {
  return (
    <Routes>
      <Route path="/" element={<Navigate to="/produto" replace />} />
      <Route path="/produto" element={<Produtos />} />
      <Route path="/produto/criar" element={<ProdutoForm />} />
      <Route path="/produto/:id" element={<ProdutoForm />} />
    </Routes>
  )
}

export default AppRoutes