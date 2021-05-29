$(function() {
    $("#friend_form1").submit(function(event) {
        // Stop form from submitting normally
        event.preventDefault();
        var friendForm = $(this);
        // Send the data using post
        var posting = $.post( friendForm.attr('action'), friendForm.serialize() );
        // if success:
        posting.done(function(data) {
                 $(friendForm)[0].reset()
        });
        // if failure:
        posting.fail(function(data) {
            // 4xx or 5xx response, alert user about failure
        });
    });

    $(".comment").submit(function(event) {
        // Stop form from submitting normally
        event.preventDefault();
        var friendForm = $(this);
        // Send the data using post
        var posting = $.post( friendForm.attr('action'), friendForm.serialize() );
        // if success:
        posting.done(function(data) {
        $(friendForm)[0].reset()

        });
        // if failure:
        posting.fail(function(data) {
            // 4xx or 5xx response, alert user about failure
        });
    });


});

$('#friend_form1').submit(function(event){
var id;
id = $(this).attr("data-catid");
$.ajax(
{
    type:"POST",
    url: "fr_request",
    data:{
             book_id: id
},success: function( data )
{
$(this)[0].reset()
    $( '#like'+ id ).removeClass('btn btn-primary btn-lg');
    $( '#like'+ id ).addClass('btn btn-success btn-lg'); } }) });


