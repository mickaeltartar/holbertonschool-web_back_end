function getStudentIdsSum(ids) {
  return ids.reduce((sum, student) => sum + student.id, 0);
}

export default getStudentIdsSum;
