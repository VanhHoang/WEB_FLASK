// click xem thêm

document.querySelector(".btn-more").onclick = () => {
  document.querySelector(".search-list-item").classList.toggle("active");
  document.querySelector(".search-item").classList.toggle("active");
};

// xử lý item của đơn hàng
var x = document.querySelector(".layer-icon");

items = document.querySelectorAll(".search-list-item .search_container");
items.forEach((item, index) => {
  item.onclick = () => {
    var value = item.textContent.trim();
    console.log("value : ", value);
    arr = value.split(":");

    document.querySelector("#name_product").value = arr[0];
    document.querySelector("#name_price").value = arr[1];

    document.querySelector(".layer").classList.add("active");
    x.onclick = () => {
      document.querySelector(".layer.active").classList.remove("active");
    };
  };
});
