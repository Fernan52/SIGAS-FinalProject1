import React from "react";
import { BrowserRouter as Router, Route, Routes, Navigate } from "react-router-dom";
import HomePage from "./pages/HomePage";
import LoginForm from "./components/LoginForm";
import RegisterForm from "./components/RegisterForm";
import ProductListPage from "./pages/ProductListPage";
import CartPage from "./pages/CartPage";
import PurchaseHistoryPage from "./pages/PurchaseHistoryPage"; // Import PurchaseHistoryPage
import InventoryPage from "./pages/InventoryPage"; // Import InventoryPage
import "./App.css";

const App = () => {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/" element={<Navigate to="/login" />} />
          <Route path="/login" element={<LoginForm />} />
          <Route path="/register" element={<RegisterForm />} />
          <Route path="/products" element={<ProductListPage />} />
          <Route path="/home" element={<HomePage />} />
          <Route path="/cart" element={<CartPage />} />
          <Route path="/purchase-history" element={<PurchaseHistoryPage />} />
          <Route path="/inventory" element={<InventoryPage />} /> {/* Add the new route */}
        </Routes>
      </div>
    </Router>
  );
};

export default App;
