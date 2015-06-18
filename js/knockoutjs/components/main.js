require(['knockout', 'autobahn', 'worker'], function (ko, autobahn, WorkerOverview) {
    console.log("HERE", ko, autobahn, WorkerOverview);

    var worker1 = new WorkerOverview();

    ko.components.register('worker-overview', {
        require: 'components/worker_overview/worker_overview.js'
    });

    ko.applyBindings({wo1: worker1});

/*

    console.log(wo.is_running());
    console.log(wo.cpu_affinity());

    wo.update({cpu_affinity: 5}).then(
        function () {
            console.log("CPU affinity set");
            console.log(wo.cpu_affinity());
        },
        function (err)                 {
            console.log("Error", err);
        }
    );
*/    
});
