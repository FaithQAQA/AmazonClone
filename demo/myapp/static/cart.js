function addItemToCart(itemId) {
  const form = document.getElementById(`add-to-cart-form-${itemId}`);
  const quantity = parseInt(form.querySelector('input[name="quantity"]').value);

  if (!isNaN(quantity) && quantity > 0 && quantity <= parseInt(form.querySelector('input[name="quantity"]').max)) {
    fetch(`/add_to_cart/${itemId}/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': form.querySelector('#csrf_token').value
      },
      body: JSON.stringify({ quantity })
    })
    .then(response => {
      if (response.ok) {
        alert('Item added to cart!');
      } else {
        alert('Failed to add item to cart.');
      }
    })
    .catch(error => {
      console.error('Error:', error);
      alert('Failed to add item to cart.');
    });
  } else {
    alert('Invalid quantity or quantity exceeds stock.');
  }
}