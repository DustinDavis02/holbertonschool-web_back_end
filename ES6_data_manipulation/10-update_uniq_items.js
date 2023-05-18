export default function updateUniqueItems(map) {
  // Check if the argument provided is a Map
  if (!(map instanceof Map)) {
    throw Error('Cannot process');
  }

  // Iterate over each entry in the map
  for (const [key, value] of map.entries()) {
    // If the value is 1, update it to 100
    if (value === 1) {
      map.set(key, 100);
    }
  }

  return map;
}
