```
//ENTITY AMBIENTE
package com.persona.Backend.Entity.Parameter.Infraestrutura;

import com.persona.Backend.Entity.BaseEntity;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Table;

@Entity
@Table(name = "especialidad")
public class Especialidad extends BaseEntity {

	@Column(name = "codigo", length = 10, nullable = false)
	private String codigo;

	@Column(name = "nombre", length = 45, nullable = false)
	private String nombre;

	@Column(name = "descripcion", length = 65, nullable = false)
	private String descripcion;

	public String getCodigo() {
		return codigo;
	}

	public void setCodigo(String codigo) {
		this.codigo = codigo;
	}

	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public String getDescripcion() {
		return descripcion;
	}

	public void setDescripcion(String descripcion) {
		this.descripcion = descripcion;
	}

}
//IREPOSITORY ESPECIALIDAD
package com.persona.Backend.IRepository.Parameter.Infraestructura;

import org.springframework.stereotype.Repository;

import com.persona.Backend.Entity.Parameter.Infraestrutura.Especialidad;
import com.persona.Backend.IRepository.IBaseRepository;

@Repository
public interface IEspecialidadRepository extends IBaseRepository<Especialidad, Long>{

}
//ISERVICE ESPECIALIDAD 
package com.persona.Backend.IService.Parameter.Infraestructura;

import com.persona.Backend.Entity.Parameter.Infraestrutura.Especialidad;
import com.persona.Backend.IService.IBaseService;

public interface IEspecialidadService extends IBaseService<Especialidad>{

}
//SERVICE ESPECIALIDAD
package com.persona.Backend.Service.Parameter.Infraestructura;

import org.springframework.stereotype.Service;

import com.persona.Backend.Entity.Parameter.Infraestrutura.Especialidad;
import com.persona.Backend.IService.Parameter.Infraestructura.IEspecialidadService;
import com.persona.Backend.Service.BaseService;

@Service
public class EspecialidadService extends BaseService<Especialidad> implements IEspecialidadService{

}
//CONTROLLER ESPECIALIDAD
package com.persona.Backend.Controller.Parameter.Infraestructura;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.persona.Backend.Controller.BaseController;
import com.persona.Backend.Entity.Parameter.Infraestrutura.Especialidad;

@CrossOrigin("*")
@RestController
@RequestMapping("/api/v1/base/parameter/infraestructura/Especialidad")
public class EspecialidadController extends BaseController<Especialidad> {

}

```