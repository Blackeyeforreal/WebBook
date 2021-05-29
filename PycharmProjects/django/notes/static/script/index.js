function show(n){
    var cards = document.getElementsByClassName("book-text");
    console.log(cards);

    var i ;
    for(i=0;i<cards.length; i++) {
      cards[i].style.display = "none";
    }
    cards[n-1].style.display = "block";
}


function show2(n){
    var cards = document.getElementsByClassName("pdf-text");
    console.log(cards);

    var i ;
    for(i=0;i<cards.length; i++) {
      cards[i].style.display = "none";
    }
    cards[n-1].style.display = "block";
}

$(function() {
    $(".books-atr").click(function(event) {
        // Stop form from submitting normally
        event.preventDefault();
        var friendForm = $(this);
        // Send the data using post
        var posting = $.post( friendForm.attr('href'));
        // if success:
        posting.done(function(data) {

            // success actions, maybe change submit button to 'friend added' or whatever
        });
        // if failure:
        posting.fail(function(data) {
            // 4xx or 5xx response, alert user about failure
        });
    });
});

function delete_Show() {
    var cross = document.getElementsByClassName("bcross");
    var i ;
     if (cross[4].style.display == "none")
    {
        for(i=0;i<cross.length; i++) {
          cross[i].style.display = "block";
        }}
        else{
        for(i=0;i<cross.length; i++) {
          cross[i].style.display = "none";
        }}

};

$(function() {
$('.bcross').click(function(){
var id;
id = $(this).attr("data-catid");
$.ajax(
{
    type:"GET",
    url: "dele",
    data:{
             book_id: id
},success: function( data )
{
    $( '#like'+ id ).removeClass('btn btn-primary btn-lg');
    $( '#like'+ id ).addClass('btn btn-success btn-lg'); } }) }) });


$(function() {
    $(".b_link").click(function(event) {
        // Stop form from submitting normally
        event.preventDefault();
        var friendForm = $(this);
        // Send the data using post
        var posting = $.post( friendForm.attr('href'));
        // if success:
        posting.done(function(data) {
            // success actions, maybe change submit button to 'friend added' or whatever
        });
        // if failure:
        posting.fail(function(data) {
            // 4xx or 5xx response, alert user about failure
        });
    });
});

$('.rec').click(function(){
var id;
id = $(this).attr("data-catid");
$.ajax(
{
    type:"GET",
    url: "breq",
    data:{
             book_id: id
}
 }) });


