```
//ENTITY FASE
package com.persona.Backend.Entity.Operational.PlanificacionFormativa;

import com.persona.Backend.Entity.BaseEntity;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.FetchType;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.Table;

@Entity
@Table(name = "fase")
public class Fase extends BaseEntity {

	@Column(name = "codigo", length = 45, nullable = false)
	private String codigo;

	@Column(name = "nombre", length = 45, nullable = false)
	private String nombre;

	@Column(name = "descripcion", length = 45, nullable = false)
	private String descripcion;

	@ManyToOne(fetch = FetchType.EAGER, optional = false)
	@JoinColumn(name = "proyecto_formativo_id", nullable = false, unique = false)
	private ProyectoFormativo proyectoFormativoId;

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

	public ProyectoFormativo getProyectoFormativoId() {
		return proyectoFormativoId;
	}

	public void setProyectoFormativoId(ProyectoFormativo proyectoFormativoId) {
		this.proyectoFormativoId = proyectoFormativoId;
	}

}
//IREPOSITORY FASE
package com.persona.Backend.IRepository.Operational.PlanificacionFormativa;

import org.springframework.stereotype.Repository;

import com.persona.Backend.Entity.Operational.PlanificacionFormativa.Fase;
import com.persona.Backend.IRepository.IBaseRepository;

@Repository
public interface IFaseRepository extends IBaseRepository<Fase, Long>{

}
//ISERVICE FASE
package com.persona.Backend.IService.Operational.PlanificacionFormativa;

import com.persona.Backend.Entity.Operational.PlanificacionFormativa.Fase;
import com.persona.Backend.IService.IBaseService;

public interface IFaseService extends IBaseService<Fase>{

}
//SERVICE FASE
package com.persona.Backend.Service.Operational.PlanificacionFormativa;

import org.springframework.stereotype.Service;

import com.persona.Backend.Entity.Operational.PlanificacionFormativa.Fase;
import com.persona.Backend.IService.Operational.PlanificacionFormativa.IFaseService;
import com.persona.Backend.Service.BaseService;

@Service
public class FaseService extends BaseService<Fase> implements IFaseService{

}
//CONTROLLER FASE
package com.persona.Backend.Controller.Operational.PlanificacionFormativa;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.persona.Backend.Controller.BaseController;
import com.persona.Backend.Entity.Operational.PlanificacionFormativa.Fase;

@CrossOrigin("*")
@RestController
@RequestMapping("/api/v1/base/operational/planificacion_formativa/fase")
public class FaseController extends BaseController<Fase> {

}


```