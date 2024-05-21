function getStudentsByLocation(ids, city) {
  if (!Array.isArray(ids)) {
    return [];
  }
  if (typeof city !== 'string') {
    throw new Error('The city parameter must be a string.');
  }
  return ids.filter((id) => id.location === city);
}

export default getStudentsByLocation;
