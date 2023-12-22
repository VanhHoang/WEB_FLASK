var x = document.querySelector(".layer-icon");

// thêm sản phẩm
document.querySelector(".plus_icon").onclick = () => {
  document.querySelector(".layer").classList.add("active");
  x.onclick = () => {
    document.querySelector(".layer.active").classList.remove("active");
  };
};
