$(document).ready(function(){

    $('form').on('submit',function (event) {

        $.ajax({
            data:{
                blockId:            $('#blockId').val(),
                User_ID:            $('#User_ID').val(),
                Machine_ID:         $('#Machine_ID').val(),
                MachineBookingTime: $('#MachineBookingTime').val(),
                MachineBookingDate: $('#MachineBookingDate').val(),
                DateMachineBooked:  $('#DateMachineBooked').val(),
                Room_ID:            $('#Room_ID').val(),
            },
			type : 'POST',
			url : '/process',
            success: function() {
                alert('Booking Confirmed');
            },

            error: function() {
                alert('Error occured');
            }
        });
		event.preventDefault();
	});
});