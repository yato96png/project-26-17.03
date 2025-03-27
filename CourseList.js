import React, { useEffect, useState } from 'react';
import axios from 'axios';

function CourseList() {
  const [courses, setCourses] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:5000/api/courses')
      .then(response => setCourses(response.data))
      .catch(error => console.error('Ошибка при загрузке курсов', error));
  }, []);

  return (
    <div>
      <h1>Список курсов</h1>
      {courses.map(course => (
        <div key={course.id}>
          <h2>{course.title}</h2>
          <p>{course.description}</p>
          <p>Цена: ${course.price}</p>
        </div>
      ))}
    </div>
  );
}

export default CourseList;
