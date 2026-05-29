import { useEffect, useState } from "react";
import "./index.css";

function App() {
  const API_URL = "/products/";

  const [products, setProducts] = useState([]);
  const [formData, setFormData] = useState({
    name: "",
    price: "",
    quantity: "",
  });

  const [editId, setEditId] = useState(null);

  const getProducts = async () => {
    const response = await fetch(API_URL);
    const data = await response.json();
    setProducts(data);
  };

  useEffect(() => {
    getProducts();
  }, []);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (editId) {
      await fetch(`${API_URL}${editId}`, {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      });

      setEditId(null);
    } else {
      await fetch(API_URL, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      });
    }

    setFormData({
      name: "",
      price: "",
      quantity: "",
    });

    getProducts();
  };

  const handleEdit = (product) => {
    setEditId(product.id);
    setFormData({
      name: product.name,
      price: product.price,
      quantity: product.quantity,
    });
  };

  return (
    <div className="app">
      <nav className="navbar">
        <h1>Product Catalog</h1>
        <p>Product Management Dashboard</p>
      </nav>

      <main className="container">
        <section className="card">
          <h2>{editId ? "Edit Product" : "Add Product"}</h2>

          <form onSubmit={handleSubmit} className="form">
            <input
              type="text"
              name="name"
              placeholder="Product name"
              value={formData.name}
              onChange={handleChange}
              required
            />

            <input
              type="number"
              name="price"
              placeholder="Price"
              value={formData.price}
              onChange={handleChange}
              required
            />

            <input
              type="number"
              name="quantity"
              placeholder="Quantity"
              value={formData.quantity}
              onChange={handleChange}
              required
            />

            <button type="submit">
              {editId ? "Update Product" : "Add Product"}
            </button>
          </form>
        </section>

        <section className="card">
          <h2>Current Product Listing</h2>

          <table>
            <thead>
              <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Price</th>
                <th>Quantity</th>
                <th>Edit</th>
              </tr>
            </thead>

            <tbody>
              {products.map((product) => (
                <tr key={product.id}>
                  <td>{product.id}</td>
                  <td>{product.name}</td>
                  <td>${product.price}</td>
                  <td>{product.quantity}</td>
                  <td>
                    <button
                      className="edit-btn"
                      onClick={() => handleEdit(product)}
                    >
                      Edit
                    </button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>

          {products.length === 0 && <p>No products found.</p>}
        </section>
      </main>
    </div>
  );
}

export default App;