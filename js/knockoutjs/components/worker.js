define(['knockout', 'autobahn'], function (ko, autobahn) {

    function WorkerOverview () {
        // local model of backend data
        //
        this.is_running = ko.observable(true);
        this.cpu_affinity = ko.observable(0);
    }

    WorkerOverview.prototype.update = function (changeset) {
        console.log("WorkerOverview.update", changeset);

        var d = autobahn.when.defer();

        if (changeset.cpu_affinity !== undefined) {
            if (this.cpu_affinity() !== changeset.cpu_affinity) {
                if (changeset.cpu_affinity >= 0 && changeset.cpu_affinity <= 7) {
                    this.cpu_affinity(changeset.cpu_affinity);
                    d.resolve(changeset.cpu_affinity);
                } else {
                    d.reject("out of range");
                }
            }
            else {
                d.resolve();
            }
        }
        return d.promise;
    }

    return WorkerOverview;
});
