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
        </tr>
    )
}

const ProjectList = ({ projects }) => {

    return (
        <table>
            <th>
                Name
            </th>
            <th>
                Author
            </th>
            {projects.map((project) => <ProjectItem project={project} />)}
        </table>
    )
}

export default ProjectList;