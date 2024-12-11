```
//ENTITY AMBIENTE
package com.persona.Backend.Entity.Parameter.Infraestrutura;

import com.persona.Backend.Entity.BaseEntity;
import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.FetchType;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.Table;

@Entity
@Table(name = "ambiente")
public class Ambiente extends BaseEntity {

	@Column(name = "codigo", length = 45, nullable = false)
	private String codigo;

	@Column(name = "nombre", length = 45, nullable = false)
	private String nombre;

	@Column(name = "cupo", length = 45, nullable = false)
	private Integer cupo;

	@ManyToOne(fetch = FetchType.EAGER, optional = false)
	@JoinColumn(name = "piso_id", nullable = false, unique = false)
	private Piso pisoId;

	@ManyToOne(fetch = FetchType.EAGER, optional = false)
	@JoinColumn(name = "especialidad_id", nullable = false, unique = false)
	private Especialidad especialidadId;

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

	public Integer getCupo() {
		return cupo;
	}

	public void setCupo(Integer cupo) {
		this.cupo = cupo;
	}

	public Piso getPisoId() {
		return pisoId;
	}

	public void setPisoId(Piso pisoId) {
		this.pisoId = pisoId;
	}

	public Especialidad getEspecialidadId() {
		return especialidadId;
	}

	public void setEspecialidadId(Especialidad especialidadId) {
		this.especialidadId = especialidadId;
	}



}
//IREPOSITORY AMBIENTE
package com.persona.Backend.IRepository.Parameter.Infraestructura;

import org.springframework.stereotype.Repository;

import com.persona.Backend.Entity.Parameter.Infraestrutura.Ambiente;
import com.persona.Backend.IRepository.IBaseRepository;

@Repository
public interface IAmbienteRepository extends IBaseRepository<Ambiente, Long>{

}
//ISERVICE AMBIENTE
package com.persona.Backend.IService.Parameter.Infraestructura;

import com.persona.Backend.Entity.Parameter.Infraestrutura.Ambiente;
import com.persona.Backend.IService.IBaseService;


public interface IAmbienteService extends IBaseService<Ambiente> {

}
//SERVICE AMBIENTE
package com.persona.Backend.Service.Parameter.Infraestructura;

import org.springframework.stereotype.Service;

import com.persona.Backend.Entity.Parameter.Infraestrutura.Ambiente;
import com.persona.Backend.IService.Parameter.Infraestructura.IAmbienteService;
import com.persona.Backend.Service.BaseService;

@Service
public class AmbienteService extends BaseService<Ambiente> implements IAmbienteService  {

}
//CONTROLLER AMBIENTE
package com.persona.Backend.Controller.Parameter.Infraestructura;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.persona.Backend.Controller.BaseController;
import com.persona.Backend.Entity.Parameter.Infraestrutura.Ambiente;

@CrossOrigin("*")//permite que cualquier dominio tenga acceso a el
@RestController
@RequestMapping("/api/v1/base/parameter/infraestructura/ambiente")
public class AmbienteController extends BaseController<Ambiente> {

}


```