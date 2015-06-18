define(['knockout', 'text!./worker_overview.html'], function (ko, htmlString) {

    function WorkerOverviewViewModel (params) {
        console.log("HERE 2", params);

        var self = this;

        // view model of visual component
        //
        this.is_running = ko.computed(function () {
            return params.worker.is_running();
        }, this);

        this.cpu_affinity = ko.computed({
            read: function () {
                return params.worker.cpu_affinity();
            },
            write: function (value) {
                console.log("write", value);

                params.worker.update({cpu_affinity: value}).then(
                    function () {
                    },
                    function (err) {
                        console.log(err);
                    }
                );
            },
            owner: this
        });
    }

    return {
        viewModel: WorkerOverviewViewModel,
        template: htmlString
    };
});
