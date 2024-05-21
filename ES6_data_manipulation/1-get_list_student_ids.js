function getListStudentIds(ids) {
  if (!Array.isArray(ids)) {
    return [];
  }
  return ids.map((newArray) => newArray.id);
}

export default getListStudentIds;
