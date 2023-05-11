export default function createReportObject(employeesList) {
  return {
    allEmployees: employeesList,
    getNumberOfDepartments: function() {
      return Object.keys(this.allEmployees).length;
    },
  };
}
