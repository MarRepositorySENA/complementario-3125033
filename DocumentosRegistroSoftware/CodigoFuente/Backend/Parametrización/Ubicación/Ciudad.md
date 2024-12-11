```
//ENTIDAD CIUDAD
package com.persona.Backend.Entity.Parameter.Ubicacion;

import com.persona.Backend.Entity.BaseEntity;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.FetchType;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.Table;

@Entity
@Table(name = "ciudad")
public class Ciudad extends BaseEntity {

	@Column(name = "nombre", length = 45, nullable = false)
	private String nombre;

	@Column(name = "codigo", length = 45, nullable = false)
	private String codigo;

	@ManyToOne(fetch = FetchType.EAGER, optional = false)
	@JoinColumn(name = "departamento_id", nullable = false, unique = false)
	private Departamento departamentoId;

	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public String getCodigo() {
		return codigo;
	}

	public void setCodigo(String codigo) {
		this.codigo = codigo;
	}

	public Departamento getDepartamentoId() {
		return departamentoId;
	}

	public void setDepartamentoId(Departamento departamentoId) {
		this.departamentoId = departamentoId;
	}

}
//IREPOSITORY CIUDAD
package com.persona.Backend.IRepository.Parameter.Ubicacion;

import com.persona.Backend.Entity.Parameter.Ubicacion.Ciudad;
import com.persona.Backend.IRepository.IBaseRepository;

public interface ICiudadRepository extends IBaseRepository<Ciudad, Long> {

}
//ISERVICE CIUDAD
package com.persona.Backend.IService.Parameter.Ubicacion;

import com.persona.Backend.Entity.Parameter.Ubicacion.Ciudad;
import com.persona.Backend.IService.IBaseService;

public interface ICiudadService extends IBaseService<Ciudad>{

}
//SERVICE CIUDAD 
package com.persona.Backend.Service.Parameter.Ubicacion;

import org.springframework.stereotype.Service;

import com.persona.Backend.Entity.Parameter.Ubicacion.Ciudad;
import com.persona.Backend.IService.Parameter.Ubicacion.ICiudadService;
import com.persona.Backend.Service.BaseService;

@Service
public class CiudadService extends BaseService<Ciudad> implements ICiudadService {

}
// CONTROLLER CIUDAD
package com.persona.Backend.Controller.Parameter.Ubicacion;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.persona.Backend.Controller.BaseController;
import com.persona.Backend.Entity.Parameter.Ubicacion.Ciudad;

@CrossOrigin("*")
@RestController
@RequestMapping("/api/v1/base/parameter/ubicacion/ciudad")
public class CiudadController extends BaseController<Ciudad> {

}


```