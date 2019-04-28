// var list_answer_question = [];

$(document).ready(function () {
    // Add class khi click chạn đáp án và lấy ra id câu hỏi, đáp án
    $(".text_answer").click(function () {
        $(this)
            .find(".choose_Answer")
            .addClass("active");
        $(this)
            .parents(".form-group")
            .siblings()
            .find(".text_answer .choose_Answer")
            .removeClass("active");
        $(this).addClass("active");
        $(this)
            .parents(".form-group")
            .siblings()
            .find(".text_answer ")
            .removeClass("active");

        // var value_id_answer = $(this).data("answer_id");

        // var value_id_question = $(this)
        //     .parents(".QA-item")
        //     .find(".question_number")
        //     .data("question_id");

        // var filter = list_answer_question.find(
        //     x => x.id_question == value_id_question
        // );

        // if (filter != undefined) {
        //     list_answer_question.splice(list_answer_question.indexOf(filter), 1);
        // }
        // list_answer_question.push({
        //     id_question: value_id_question,
        //     id_answer: value_id_answer
        // });

        // console.log(list_answer_question);
    });
});

$(document).on("submit", "#list_question_answer", function (e) {
    e.preventDefault();

    var id_exam = $("#id_exam").val();
    var total_question = $('#total_question').val();

    var thisForm = $(this);
    var action = thisForm.attr("action");
    var method = thisForm.attr("method");

    var list_answer_question = $(this).serializeArray();
    list_answer_question.shift();

    var complete = 1;

    var data = JSON.stringify({
        id_exam: id_exam,
        complete: complete,
        total_question: total_question,
        list_answer_question: list_answer_question
    });

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== "") {
            var cookies = document.cookie.split(";");
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === name + "=") {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie("csrftoken");

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return /^(GET|HEAD|OPTIONS|TRACE)$/.test(method);
    }

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    $.ajax({
        type: method,
        url: action,
        dataType: "json",
        contentType: "application/json",
        data: data,
        success: function (response) {

            $('#show-popup').click();

            $('#result_link').on('click', function () {
                window.location.href = '/result/detail/' + response.id + '/' + response.key;
            });

            $('#home_link').on('click', function () {
                window.location.href = '/';
            });

        },
    });
});

var value_time = $("#total_time_to_do_exam").val();
var c = value_time * 60;
var t;
timedCount();

function timedCount() {
    var hours = parseInt(c / 3600) % 24;
    var minutes = parseInt(c / 60) % 60;
    var seconds = c % 60;

    var result =
        (hours < 10 ? "0" + hours : hours) +
        ":" +
        (minutes < 10 ? "0" + minutes : minutes) +
        ":" +
        (seconds < 10 ? "0" + seconds : seconds);

    $("#countdown").html(result);

    if (c == 0) {
        Swal.fire({
            type: 'error',
            title: 'Đã hết thời gian làm bài',
            text: 'Vui lòng nộp bài thi !!!',
            allowOutsideClick: false,
            closeOnClickOutside: false,
        })
        $(".text_answer").addClass("disabled");
    }

    c = c - 1;
    t = setTimeout(function () {
        timedCount();
    }, 1000);

    if (hours == 0 && minutes == 0 && seconds == 0) {
        clearTimeout(t);
    }
}
