import React from "react";


const ProjectItem = ({ project }) => {

    return (
        <tr>
            <td>
                {project.name}
            </td>
            <td>
                {project.author}
            </td>
            <td><button onClick={() => deleteProject(item.id)}
                type='button'>Delete</button>
            </td>
        </tr>
    )
}

const ProjectList = ({ projects }) => {

    return (
        <div>
            <table>
                <th>
                    Name
                </th>
                <th>
                    Author
                </th>
                {projects.map((project) => <ProjectItem project={project} deleteProject={deleteProject} />)}
            </table>
            <Link to='/projects/create'>Create</Link>
        </div>
    )
}

export default ProjectList;