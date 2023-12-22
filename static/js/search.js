// $(document).ready(function () {
//   document.querySelector("#searchSubmit").onclick = (event) => {
//     event.preventDefault(); // ngăn chặn hành vi load lại trang
//     event.stopPropagation(); // Ngăn chặn hành vi mặc định của các sự kiện cha
//     var keyword = document.getElementById("searchInput").value;
//     console.log(keyword);

//     $.ajax({
//       url: "/search",
//       type: "GET",
//       data: {
//         keyword: keyword,
//       },
//       success: (data) => {
//         $("#searchResults tbody").html(data);
//         console.log(data);
//       },
//     });
//   };
// });

// khi click
$(document).ready(function () {
  document.querySelector("#searchSubmit").onclick = (event) => {
    event.preventDefault(); // ngăn chặn hành vi load lại trang
    event.stopPropagation(); // Ngăn chặn hành vi mặc định của các sự kiện cha
    var keyword = document.getElementById("searchInput").value.trim();
    console.log(keyword);

    $.ajax({
      url: "/search",
      type: "GET",
      data: {
        keyword: keyword,
      },
      success: function (data) {
        var tableHtml = "";
        data.forEach(function (item) {
          tableHtml +=
            "<tr><th scope='row'>" +
            item.id +
            "</th><td>" +
            item.name +
            "</td><td>" +
            item.product +
            "</td><td>" +
            item.price +
            "</td><td>" +
            item.number +
            "</td><td>" +
            item.phone +
            "</td><td>" +
            item.email +
            "</td><td><button class='btn-primary'><a style='color: white' href='/update_order/" +
            item.id +
            "'>Sửa</a></button></td><td><button class='btn-warning'><a style='color: white' href='/delete_order/" +
            item.id +
            "'>Xóa</a></button></td></tr>";
        });
        console.log(tableHtml);
        $("#searchResults tbody").html(tableHtml);
      },
    });
  };
});

// khi oninput
$(document).ready(function () {
  document.querySelector("#searchInput").onclick = (event) => {
    event.preventDefault(); // ngăn chặn hành vi load lại trang
    event.stopPropagation(); // Ngăn chặn hành vi mặc định của các sự kiện cha
    var keyword = document.getElementById("searchInput").value.trim();
    console.log(keyword);

    $.ajax({
      url: "/search",
      type: "GET",
      data: {
        keyword: keyword,
      },
      success: function (data) {
        var tableHtml = "";
        data.forEach(function (item) {
          tableHtml +=
            "<tr><th scope='row'>" +
            item.id +
            "</th><td>" +
            item.name +
            "</td><td>" +
            item.product +
            "</td><td>" +
            item.price +
            "</td><td>" +
            item.number +
            "</td><td>" +
            item.phone +
            "</td><td>" +
            item.email +
            "</td><td><button class='btn-primary'><a style='color: white' href='/update_order/" +
            item.id +
            "'>Sửa</a></button></td><td><button class='btn-warning'><a style='color: white' href='/delete_order/" +
            item.id +
            "'>Xóa</a></button></td></tr>";
        });
        console.log(tableHtml);
        $("#searchResults tbody").html(tableHtml);
      },
    });
  };
});
