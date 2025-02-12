import React from "react";
import "../styles/ProjectInfo.css";

const ProjectInfo = () => {
  return (
    <div className="project-info-container">
      <h2>About SIGAS</h2>
      <p>
        SIGAS (Sistema de Gestión de Almacén y Supermercado) is a comprehensive
        system designed to manage the inventory, sales, and customer interactions
        of a supermarket. It includes features such as product management, cart
        management, purchase history, and product reviews.
      </p>
      <h3>Features:</h3>
      <ul>
        <li>Product Management: Add, update, and delete products from the inventory.</li>
        <li>Cart Management: Add products to the cart, update quantities, and remove items.</li>
        <li>Purchase History: View the history of purchases made by customers.</li>
        <li>Product Reviews: Allow customers to leave reviews and ratings for products.</li>
      </ul>
      <h3>Technologies Used:</h3>
      <ul>
        <li>Frontend: React, CSS</li>
        <li>Backend: Flask, MongoDB</li>
        <li>Containerization: Docker</li>
      </ul>
    </div>
  );
};

export default ProjectInfo;