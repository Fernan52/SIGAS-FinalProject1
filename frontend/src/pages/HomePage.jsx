import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import SearchProducts from "../components/SearchProducts";
import ProjectInfo from "../components/ProjectInfo"; // Import the ProjectInfo component
import "../styles/Home.css";

const HomePage = () => {
  const categories = [
    "Fruits",
    "Vegetables",
    "Snacks",
    "Beverages",
    "Meat",
    "Dairy",
    "Bakery",
    "Frozen",
    "Cleaning",
    "Baby",
  ];

  const [selectedCategory, setSelectedCategory] = useState("Fruits");
  const [isCartEmpty, setIsCartEmpty] = useState(true);
  const navigate = useNavigate();

  useEffect(() => {
    const fetchCartState = async () => {
      const username = localStorage.getItem("username");
      if (!username) {
        setIsCartEmpty(true);
        return;
      }

      try {
        const response = await fetch(`http://54.174.103.161:4005/get_cart/${username}`, {
          method: "GET",
          headers: {
            "Content-Type": "application/json",
          },
        });

        if (!response.ok) {
          throw new Error("Failed to fetch cart data");
        }

        const data = await response.json();
        setIsCartEmpty(!data.cart || data.cart.length === 0);
      } catch (error) {
        console.error("Error fetching cart state:", error);
        setIsCartEmpty(true);
      }
    };

    fetchCartState();
  }, []);

  const handleCartUpdate = () => {
    setIsCartEmpty(false);
  };

  const handleLogout = () => {
    localStorage.clear();
    navigate("/login");
  };

  return (
    <div className="main-container">
      <header className="header">
        <h1>SIGAS - Supermaxi</h1>
        <button className="logout-button" onClick={handleLogout}>
          Logout
        </button>
      </header>

      <div className="content">
        <nav className="categories-bar">
          {categories.map((category) => (
            <button
              key={category}
              className={`category-button ${category === selectedCategory ? "active" : ""}`}
              onClick={() => setSelectedCategory(category)}
            >
              {category}
            </button>
          ))}
        </nav>

        <div className="main-content">
          <div className="sidebar">
            <h2>Shopping Cart</h2>
            {isCartEmpty ? (
              <p>Your cart is empty!</p>
            ) : (
              <button onClick={() => navigate("/cart")} className="view-cart-button">
                View Cart
              </button>
            )}
            <button onClick={() => navigate("/purchase-history")} className="view-history-button">
              View Purchase History
            </button>
            <button onClick={() => navigate("/inventory")} className="view-inventory-button">
              Manage Inventory
            </button>
            <button onClick={() => navigate("/reviews")} className="view-reviews-button">
              View Product Reviews
            </button>
          </div>

          <div className="products-container">
            <SearchProducts selectedCategory={selectedCategory} onCartUpdate={handleCartUpdate} />
          </div>
        </div>
      </div>

      <footer className="footer">
        <ProjectInfo /> {/* Add the ProjectInfo component here */}
      </footer>
    </div>
  );
};

export default HomePage;