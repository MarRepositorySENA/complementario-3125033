```
//ENTITY PROGRAMAFORMACION 
package com.persona.Backend.Entity.Operational.GestionFormativa;

import com.persona.Backend.Entity.BaseEntity;

import jakarta.persistence.*;

@Entity
@Table(name="programa_formacion")
public class ProgramaFormacion extends BaseEntity{

	@Column(name = "nombre", length = 45, nullable = false)
	private String nombre;
	
	@Column(name = "descripcion", length = 45, nullable = false)
	private String descripcion;
	
	@Column(name = "duraccion", length = 45, nullable = false)
	private Integer duraccion;
	
	@ManyToOne(fetch = FetchType.EAGER, optional = false)
	@JoinColumn(name = "modalidad_id", nullable = false, unique = false)
	private Modalidad modalidadId;
	
	@ManyToOne(fetch = FetchType.EAGER, optional = false)
	@JoinColumn(name = "nivel_formacion_id", nullable = false, unique = false)
	private NivelFormacion nivelFormacionId;
	
	@ManyToOne(fetch = FetchType.EAGER, optional = false)
	@JoinColumn(name = "tipo_formacion_id", nullable = false, unique = false)
	private TipoFormacion tipoFormacionId;

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

	public Integer getDuraccion() {
		return duraccion;
	}

	public void setDuraccion(Integer duraccion) {
		this.duraccion = duraccion;
	}

	public Modalidad getModalidadId() {
		return modalidadId;
	}

	public void setModalidadId(Modalidad modalidadId) {
		this.modalidadId = modalidadId;
	}

	public NivelFormacion getNivelFormacionId() {
		return nivelFormacionId;
	}

	public void setNivelFormacionId(NivelFormacion nivelFormacionId) {
		this.nivelFormacionId = nivelFormacionId;
	}

	public TipoFormacion getTipoFormacionId() {
		return tipoFormacionId;
	}

	public void setTipoFormacionId(TipoFormacion tipoFormacionId) {
		this.tipoFormacionId = tipoFormacionId;
	}
	
}
//IREPOSITORY PROGRAMAFORMACION
package com.persona.Backend.IRepository.Operational.GestionFormativa;

import org.springframework.stereotype.Repository;

import com.persona.Backend.Entity.Operational.GestionFormativa.ProgramaFormacion;
import com.persona.Backend.IRepository.IBaseRepository;

@Repository
public interface IProgramaFormacionRepository extends IBaseRepository<ProgramaFormacion, Long> {

}
//ISERVICE PROGRAMAFORMACION
package com.persona.Backend.IService.Operational.GestionFormativa;

import com.persona.Backend.Entity.Operational.GestionFormativa.ProgramaFormacion;
import com.persona.Backend.IService.IBaseService;

public interface IProgramaFormacionService extends IBaseService<ProgramaFormacion>{

}
//SERVICE PROGRAMAFORMACION
package com.persona.Backend.Service.Operational.GestionFormativa;

import org.springframework.stereotype.Service;

import com.persona.Backend.Entity.Operational.GestionFormativa.ProgramaFormacion;
import com.persona.Backend.IService.Operational.GestionFormativa.IProgramaFormacionService;
import com.persona.Backend.Service.BaseService;

@Service
public class ProgramaFormacionService extends BaseService<ProgramaFormacion> implements IProgramaFormacionService{

}
//CONTROLLER PROGRAMAFORMACION
package com.persona.Backend.Controller.Operational.GestionFormativa;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.persona.Backend.Controller.BaseController;
import com.persona.Backend.Entity.Operational.GestionFormativa.ProgramaFormacion;

@CrossOrigin("*")
@RestController
@RequestMapping("/api/v1/base/operational/gestion_formativa/programa_formacion")
public class ProgramaFormacionController extends BaseController<ProgramaFormacion>{

}

```