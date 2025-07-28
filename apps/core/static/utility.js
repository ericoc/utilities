const xhr = new XMLHttpRequest();
xhr.open("GET", `/api/${utilityTitle.replace(" ", "_").toLowerCase()}/?format=json`);
xhr.onreadystatechange = async () => {
    if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
        const utilityUsageData = JSON.parse(xhr.responseText);

        const utilityKeys = Object.keys(utilityUsageData[0]);
        const utilityTimeName = utilityKeys[0];
        const utilityTimeDesc = (utilityTimeName.charAt(0).toUpperCase() + utilityTimeName.slice(1));
        document.getElementById('time-col').innerText = utilityTimeDesc;

        const utilityUnitName = utilityKeys[1];
        const utilityUnitDesc = (utilityUnitName.charAt(0).toUpperCase() + utilityUnitName.slice(1));
        document.getElementById('unit-col').innerText = utilityUnitDesc;

        const utilityUsageOverTime = [];
        for (const item in utilityUsageData) {
            utilityUsageOverTime.push([
                DateTime.fromISO(utilityUsageData[item][utilityTimeName]).toMillis(),
                utilityUsageData[item][utilityUnitName]
            ]);
        }

        /* Highcharts. */
        new Highcharts.Chart('utility-chart', {
            chart: { zooming: { type: 'x' } },
            credits: false,
            series: [{
                color: utilityColor,
                data: utilityUsageOverTime,
                name: utilityUnitDesc,
                states: { hover: { lineWidthPlus: 0 } },
                type: 'line'
            }],
            styledMode: true,
            time: { timezone: timeZone },
            title: {
                style: { color: '#fff' },
                text: utilityTitle,
            },
            xAxis: {
                title: { text: utilityTimeDesc },
                type: 'datetime'
            },
            yAxis: {
                title: { text: utilityUnitDesc },
                type: 'num'
            },
        });

        /* DataTables. */
        const resultName = `${utilityTimeName}s`;
        const defaultPageLength = 12;
        new DataTable('#utility-table', {
            data: utilityUsageData,
            columns: [
                {
                    data: utilityTimeName,
                    render: dataTableTimeFmt
                },
                {
                    data: utilityUnitName,
                    render: (data, type) => {
                        if (type === 'display') {
                            let utilityTextColor = 'primary';
                            if (utilityThresholds) {
                                if (data >= utilityThresholds[0]) {
                                    utilityTextColor = 'danger';
                                } else if (data >= utilityThresholds[1]) {
                                    utilityTextColor = 'warning';
                                } else if (data >= utilityThresholds[2]) {
                                    utilityTextColor = 'info';
                                }
                            }
                            return `<code class="fw-bold text-${utilityTextColor}-emphasis" title="${data} ${utilityUnitDesc}">${data}</code>`;
                        }
                        return data;
                    },
                    type: 'num'
                }
            ],
            footerCallback: async function () {
                // Calculate totals for footer.
                let api = this.api();
                let col = 1;
                let digits = 4;
                let pageUtility = DataTable.render.number(',', '.', digits).display(api.column(col, {page: 'current'}).data().sum());
                document.getElementById('page-total').innerHTML = `<span class="badge font-monospace" title="This Page: ${pageUtility} ${utilityUnitDesc}"> ${pageUtility} ${utilityUnitDesc}</span>`;
                let totalUtility = DataTable.render.number(',', '.', digits).display(api.column(col).data().sum());
                document.getElementById('all-total').innerHTML = `<span class="badge border-utility font-monospace" title="All Pages: ${totalUtility} ${utilityUnitDesc}"> ${totalUtility} ${utilityUnitDesc}</span>`;

                // Finally, hide the loading spinner.
                let chartLoading = document.getElementById('chart-loading');
                if ((chartLoading) && (chartLoading.visibility === true)) {
                    chartLoading.visibility = false;
                }
            },
            language: {
                buttons: {
                    createState: '<span class="bi bi-save" title="Save State"> Save State</span>',
                    savedStates: {
                        0: '<span class="bi bi-floppy" title="Saved States"> Saved States</span>',
                        1: '<span class="bi bi-floppy" title="Saved States (1)"> Saved States (1)</span>',
                        _: '<span class="bi bi-floppy" title="Saved States">Saved States (%d)</span>',
                    },
                },
                emptyTable: `No ${resultName} available in table`,
                info: `<span title="_START_ &mdash; _END_ / _TOTAL_ ${resultName}"><i class="bi bi-info-circle color-utility"></i> <b>_START_</b> &mdash; <b>_END_</b> / <b>_TOTAL_</b> ${resultName}</span>`,
                infoEmpty: `<span class="bi bi-patch-exclamation text-danger" title="0 ${resultName}"> <b>0</b> ${resultName}</span>`,
                infoFiltered: `<span title="(of _MAX_ total)">(of <b>_MAX_</b> total)</span>`,
                lengthMenu: `_MENU_ ${resultName}`,
                searchBuilder: {
                    button: {
                        0: '<span class="bi bi-search" title="Search"> Search</span>',
                        1: '<span class="bi bi-search" title="Search (1)"> Search (1)</span>',
                        _: '<span class="bi bi-search" title="Search"></span> Search (%d)</i>',
                    },
                    title: '<span class="bi bi-search" title="Search"> Search</span>',
                },
                zeroRecords: `No ${resultName} found`
            },
            layout: {
                topStart: {
                    buttons: [
                        {
                            extend: 'copyHtml5',
                            text: '<span class="bi bi-clipboard" title="Copy rows to clipboard"> Copy</span>'
                        },
                        {
                            extend: 'csvHtml5',
                            text: '<span class="bi bi-filetype-csv" title="Comma-Separated Values (.csv)"> CSV</span>'
                        },
                        {
                            extend: 'excelHtml5',
                            text: '<i class="bi bi-filetype-xlsx" title="Microsoft Excel (.xlsx)"></i> Excel'
                        },
                        {
                            extend: 'pdfHtml5',
                            text: '<i class="bi bi-filetype-pdf" title="Portable Data Format (.pdf)"></i> PDF'
                        },
                        {
                            extend: 'print',
                            text: '<i class="bi bi-printer" title="Print"></i> Print'
                        },
                        {
                            extend: 'searchBuilder',
                            config: { depthLimit: 1 },
                        },
                    ],
                },
                topEnd: 'pageLength',
                bottomStart: 'paging',
                bottomEnd: 'info',
            },
            lengthMenu: [
                1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
                {
                    label: `${defaultPageLength} *`,
                    value: defaultPageLength
                },
                13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
                28, 29, 30, 31, 32, 35, 36, 42, 48, 50, 60, 64, 70, 72, 84,
                96, 100, 108, 120, 132, 144, 150, 160, 180, 200, 250, 300,
                500, 750, 1000, 1500, 2000, 2500, 3000, 3600, 4000, 5000,
                7500, 10000, {label: 'All', value: -1}
            ],
            order: [[0, 'desc']],
            pageLength: defaultPageLength,
            stateSave: true
        });
    }
};
xhr.send();
