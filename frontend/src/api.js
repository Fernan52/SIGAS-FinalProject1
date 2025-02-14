import axios from "axios";

export const addToCart = async (item) => {
  try {
    const response = await axios.post("http://18.212.3.158:5000/add_product", item);
    return response.data;
  } catch (error) {
    console.error("Error adding to cart:", error.message);
    throw error;
  }
};

export const searchProducts = async (query) => {
  try {
    const response = await axios.get("http://44.202.150.206:4009/search_products", {
      params: { query },
    });
    return response.data;
  } catch (error) {
    console.error("Error searching products:", error.message);
    throw error;
  }
};

export const login = async (credentials) => {
  try {
    const response = await axios.post("http://3.87.214.25:4017/login", credentials);
    return response.data;
  } catch (error) {
    console.error("Error logging in:", error.message);
    throw error;
  }
};

export const register = async (user) => {
  try {
    const response = await axios.post("http://52.23.184.1:4018/register", user);
    return response.data;
  } catch (error) {
    console.error("Error registering user:", error.message);
    throw error;
  }
};

export const getCart = async (username) => {
  try {
    const response = await axios.get(`http://34.203.188.62:4005/get_cart/${username}`);
    return response.data;
  } catch (error) {
    console.error("Error fetching cart:", error.message);
    throw error;
  }
};

export const updateQuantity = async (username, productName, quantity) => {
  try {
    const response = await axios.patch("http://54.242.135.110:4011/update_quantity", {
      username,
      product_name: productName,
      quantity,
    });
    return response.data;
  } catch (error) {
    console.error("Error updating quantity:", error.message);
    throw error;
  }
};

export const resetCart = async (username) => {
  try {
    const response = await axios.post(`http://3.83.123.114:4008/reset_cart/${username}`);
    return response.data;
  } catch (error) {
    console.error("Error resetting cart:", error.message);
    throw error;
  }
};

export const checkout = async (username) => {
  try {
    const response = await axios.post("http://44.203.123.1:4002/checkout", { username });
    return response.data;
  } catch (error) {
    console.error("Error during checkout:", error.message);
    throw error;
  }
};

export const getPurchaseHistory = async (username) => {
  try {
    const response = await axios.get(`http://3.83.17.44:4014/purchase_history/${username}`);
    return response.data;
  } catch (error) {
    console.error("Error fetching purchase history:", error.message);
    throw error;
  }
};

export const getInventory = async () => {
  try {
    const response = await axios.get("http://44.203.168.161:4015/inventory");
    return response.data;
  } catch (error) {
    console.error("Error fetching inventory:", error.message);
    throw error;
  }
};

export const addProduct = async (product) => {
  try {
    const response = await axios.post("http://44.211.201.158:5000/add_product", product);
    return response.data;
  } catch (error) {
    console.error("Error adding product:", error.message);
    throw error;
  }
};

export const deleteProduct = async (username, productName) => {
  try {
    const response = await axios.delete("http://174.129.81.15:5001/delete_product", {
      data: { username, product_name: productName },
    });
    return response.data;
  } catch (error) {
    console.error("Error deleting product:", error.message);
    throw error;
  }
};

export const getReviews = async (productId) => {
  try {
    const response = await axios.get(`http://18.234.208.144:4016/reviews?product_id=${productId}`);
    return response.data;
  } catch (error) {
    console.error("Error fetching reviews:", error.message);
    throw error;
  }
};

export const addReview = async (review) => {
  try {
    const response = await axios.post("http://18.234.208.144:4016/reviews", review);
    return response.data;
  } catch (error) {
    console.error("Error adding review:", error.message);
    throw error;
  }
};