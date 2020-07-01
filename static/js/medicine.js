$(document).ready(function () {

    var table


    function addMedicine(data) {

        var settings = {
            "async": true,
            "crossDomain": true,
            "url": "medicine",
            "method": "POST",
            "headers": {
                "content-type": "application/json",
                "cache-control": "no-cache",
                "postman-token": "2612534b-9ccd-ab7e-1f73-659029967199"
            },
            "processData": false,
            "data": JSON.stringify(data)
        }

        $.ajax(settings).done(function (response) {
            $('.modal.in').modal('hide')
            $.notify("Added Successfully", {"status":"success"});
            table.destroy();
            $('#datatable4 tbody').empty(); // empty in case the columns change
            getMedicine()
        });

    }

    function deleteMedicine(id) {
        var settings = {
            "async": true,
            "crossDomain": true,
            "url": "medicine/" + id,
            "method": "DELETE",
            "headers": {
                "cache-control": "no-cache",
                "postman-token": "28ea8360-5af0-1d11-e595-485a109760f2"
            }
        }

swal({
    title: "Are you sure?",
    text: "You will not be able to recover this data",
    type: "warning",
    showCancelButton: true,
    confirmButtonColor: "#DD6B55",
    confirmButtonText: "Yes, delete it!",
    closeOnConfirm: false
}, function() {
 $.ajax(settings).done(function (response) {
   swal("Deleted!", "success");
            table.destroy();
            $('#datatable4 tbody').empty(); // empty in case the columns change
            getMedicine()
        });


});

    }

    function updateMedicine(data, id) {
        var settings = {
            "async": true,
            "crossDomain": true,
            "url": "medicine/" + id,
            "method": "PUT",
            "headers": {
                "content-type": "application/json",
                "cache-control": "no-cache"
            },
            "processData": false,
            "data": JSON.stringify(data)
        }

        $.ajax(settings).done(function (response) {
            $('.modal.in').modal('hide')
            $.notify("Updated Successfully", {"status":"success"});
            table.destroy();
            $('#datatable4 tbody').empty(); // empty in case the columns change
            getMedicine()
        });


    }

    function getMedicine() {

        var settings = {
            "async": true,
            "crossDomain": true,
            "url": "medicine",
            "method": "GET",
            "headers": {
                "cache-control": "no-cache"
            }
        }

        $.ajax(settings).done(function (response) {



            table = $('#datatable4').DataTable({
                "bDestroy": true,
                'paging': true, // Table pagination
                'ordering': true, // Column ordering
                'info': true, // Bottom left status text
                aaData: response,
                 "aaSorting": [],
                aoColumns: [
                  {
                      mData: 'med_name'
                  },
                  {
                      mData: 'med_power'
                  },
                  {
                      mData: 'med_brand'
                  },
                  {
                      mData: 'med_mfg'
                  },
                  {
                      mData: 'med_exp'
                  },
                  {
                      mData: 'med_quan'
                  },
                    {
                        mRender: function (o) {
                            return '<button class="btn-xs btn btn-info btn-edit" type="button">Edit</button>';
                        }
                    },
                    {
                        mRender: function (o) {
                            return '<button class="btn-xs btn btn-danger delete-btn" type="button">Delete</button>';
                        }
                    }
        ]
            });
            $('#datatable4 tbody').on('click', '.delete-btn', function () {
                var data = table.row($(this).parents('tr')).data();
                console.log(data)
                deleteMedicine(data.med_id)

            });
            $('.btn-edit').one("click", function(e) {
                var data = table.row($(this).parents('tr')).data();
                $('#myModal').modal().one('shown.bs.modal', function (e) {
                    for (var key in data) {
                        $("[name=" + key + "]").val(data[key])
                    }
                    $("#savetheMedicine").off("click").on("click", function(e) {
                    var instance = $('#detailform').parsley();
                    instance.validate()
                    console.log(instance.isValid())
                    if(instance.isValid()){
                        jsondata = $('#detailform').serializeJSON();
                        updateMedicine(jsondata, data.med_id)
                        }

                    })
                })



            });

        });


    }




    $("#addmedicine").click(function () {
$('#detailform input,textarea').val("")
        $('#myModal').modal().one('shown.bs.modal', function (e) {

console.log('innn')
            $("#savethemedicine").off("click").on("click", function(e) {
            console.log("inn")
            var instance = $('#detailform').parsley();
            instance.validate()
                    if(instance.isValid()){
                jsondata = $('#detailform').serializeJSON();
                addMedicine(jsondata)
                }

            })

        })

    })
$("#export").click(function () {
$('#detailform input,textarea').val("")
        $('#myexport').modal().one('shown.bs.modal', function (e) {

console.log('innn')
            $("#savethemedicine").off("click").on("click", function(e) {
            console.log("inn")
            var instance = $('#detailform').parsley();
            instance.validate()
                    if(instance.isValid()){
                jsondata = $('#detailform').serializeJSON();
                addMedicine(jsondata)
                }

            })

        })



    })

getMedicine()
})
